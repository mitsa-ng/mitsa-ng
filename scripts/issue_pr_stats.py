#!/usr/bin/env python3
"""Generate the per-repo "issues / PRs / merged" stats SVG panel.

Counts everything the user authored, grouped by repository, via the GitHub
Search API (paginated). Renders top-N repos plus an all-repo totals row.
Theme/layout helpers are shared with recent_prs.py.
"""

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

from recent_prs import FONT, PAD, PANEL_W, THEMES, C, esc, fit, out_path, rel_time

TOP_N = 12

L10N = {
    "zh": {
        "title": "Issue / PR 統計",
        "col_repo": "專案",
        "col_issues": "Issues",
        "col_prs": "PRs",
        "col_merged": "已合併",
        "total": "總計",
        "more": "另外 {n} 個專案",
        "empty": "還沒有資料",
        "updated": "最後更新",
    },
    "en": {
        "title": "Issue & PR stats",
        "col_repo": "Project",
        "col_issues": "Issues",
        "col_prs": "PRs",
        "col_merged": "Merged",
        "total": "Total",
        "more": "+{n} more projects",
        "empty": "Nothing here yet",
        "updated": "updated",
    },
    "ja": {
        "title": "Issue / PR 統計",
        "col_repo": "プロジェクト",
        "col_issues": "Issues",
        "col_prs": "PRs",
        "col_merged": "マージ済み",
        "total": "合計",
        "more": "他 {n} プロジェクト",
        "empty": "データはまだありません",
        "updated": "最終更新",
    },
    "fr": {
        "title": "Stats Issues & PR",
        "col_repo": "Projet",
        "col_issues": "Issues",
        "col_prs": "PRs",
        "col_merged": "Fusionnées",
        "total": "Total",
        "more": "+{n} autres projets",
        "empty": "Pas encore de données",
        "updated": "maj",
    },
}


def fetch_search(q: str) -> list:
    """Walk all pages of a GitHub Search API query (100/page, 10-page cap)."""
    items, page = [], 1
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    while True:
        url = (
            "https://api.github.com/search/issues?"
            + urllib.parse.urlencode(
                {"q": q, "per_page": 100, "page": page, "sort": "updated", "order": "desc"}
            )
        )
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "profile-stats-panel",
        })
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                batch = json.load(resp)["items"]
        except Exception as e:  # noqa: BLE001 - surface as a hard failure
            print(f"error: GitHub search API failed: {e}", file=sys.stderr)
            sys.exit(1)
        items.extend(batch)
        if len(batch) < 100 or page >= 10:
            return items
        page += 1


def collect(user: str) -> list:
    """Aggregate authored issues / PRs / merged PRs per full repo name."""
    repos: dict = {}
    for query, kind in (
        (f"is:issue author:{user}", "issue"),
        (f"is:pr author:{user}", "pr"),
    ):
        for it in fetch_search(query):
            full = "/".join(it["repository_url"].rstrip("/").rsplit("/", 2)[-2:])
            r = repos.setdefault(full, {"issues": 0, "prs": 0, "merged": 0})
            if kind == "issue":
                r["issues"] += 1
            else:
                r["prs"] += 1
                if (it.get("pull_request") or {}).get("merged_at"):
                    r["merged"] += 1
    rows = []
    for full, r in repos.items():
        owner, name = full.split("/", 1)
        display = name if (owner == user or owner == name) else full
        rows.append({"repo": display, **r})
    rows.sort(key=lambda x: (-x["prs"], -x["issues"], x["repo"]))
    return rows


def render(rows: list, lang: str, top_n: int = TOP_N) -> str:
    t = L10N[lang]
    # column anchors: numbers right-aligned; merged hugs the right edge
    x_issues, x_prs, x_merged = PANEL_W - PAD - 220, PANEL_W - PAD - 110, PANEL_W - PAD

    top = rows[:top_n]
    totals = {
        "issues": sum(r["issues"] for r in rows),
        "prs": sum(r["prs"] for r in rows),
        "merged": sum(r["merged"] for r in rows),
    }
    extra = max(len(rows) - TOP_N, 0)

    y = 84  # column header baseline
    if rows:
        height = y + 20 + len(top) * 30 + 34 + (18 if extra else 8) + 8
    else:
        height = y + 40

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{PANEL_W}" height="{height}" '
        f'viewBox="0 0 {PANEL_W} {height}" role="img">',
        f'<rect width="100%" height="100%" rx="10" fill="{C["bg"]}" stroke="{C["border"]}" stroke-width="1"/>',
        f'<style>text{{font-family:{FONT};}} .b{{font-weight:600;}}</style>',
        f'<text x="{PAD}" y="44" font-size="18" fill="{C["accent"]}" class="b">{esc(t["title"])}</text>',
        f'<text x="{PANEL_W - PAD}" y="44" font-size="11" fill="{C["muted"]}" text-anchor="end">'
        f'{esc(t["updated"])} {esc(rel_time(datetime.now(timezone.utc), lang))}</text>',
        f'<line x1="{PAD}" y1="58" x2="{PANEL_W - PAD}" y2="58" stroke="{C["sep"]}" stroke-width="1"/>',
    ]

    if not rows:
        parts.append(
            f'<text x="{PANEL_W / 2}" y="{y + 16}" font-size="13" fill="{C["muted"]}" '
            f'text-anchor="middle">{esc(t["empty"])}</text>'
        )
        parts.append("</svg>")
        return "\n".join(parts) + "\n"

    # column header row
    parts.append(f'<text x="{PAD}" y="{y}" font-size="11" fill="{C["muted"]}">{esc(t["col_repo"])}</text>')
    for x, label in ((x_issues, t["col_issues"]), (x_prs, t["col_prs"]), (x_merged, t["col_merged"])):
        parts.append(
            f'<text x="{x}" y="{y}" font-size="11" fill="{C["muted"]}" text-anchor="end">{esc(label)}</text>'
        )
    y += 16
    parts.append(
        f'<line x1="{PAD}" y1="{y}" x2="{PANEL_W - PAD}" y2="{y}" stroke="{C["sep"]}" stroke-width="1"/>'
    )

    # data rows
    for r in top:
        y += 30
        repo = fit(r["repo"], 13, x_issues - 40 - PAD)
        parts.append(
            f'<text x="{PAD}" y="{y - 8}" font-size="13" fill="{C["fg"]}" class="b">{esc(repo)}</text>'
        )
        parts.append(
            f'<text x="{x_issues}" y="{y - 8}" font-size="13" fill="{C["muted"]}" '
            f'text-anchor="end">{r["issues"]}</text>'
        )
        parts.append(
            f'<text x="{x_prs}" y="{y - 8}" font-size="13" fill="{C["fg"]}" '
            f'text-anchor="end">{r["prs"]}</text>'
        )
        merged_cls = ' class="b"' if r["merged"] else ""
        parts.append(
            f'<text x="{x_merged}" y="{y - 8}" font-size="13" '
            f'fill="{C["merged"] if r["merged"] else C["muted"]}"'
            f'{merged_cls} text-anchor="end">{r["merged"]}</text>'
        )
        parts.append(
            f'<line x1="{PAD}" y1="{y - 2}" x2="{PANEL_W - PAD}" y2="{y - 2}" '
            f'stroke="{C["sep"]}" stroke-width="1"/>'
        )

    # totals row (all repos, not just top N)
    y += 34
    parts.append(
        f'<line x1="{PAD}" y1="{y - 26}" x2="{PANEL_W - PAD}" y2="{y - 26}" '
        f'stroke="{C["border"]}" stroke-width="1"/>'
    )
    parts.append(
        f'<text x="{PAD}" y="{y - 6}" font-size="13.5" fill="{C["accent"]}" class="b">{esc(t["total"])}</text>'
    )
    for x, v in ((x_issues, totals["issues"]), (x_prs, totals["prs"]), (x_merged, totals["merged"])):
        parts.append(
            f'<text x="{x}" y="{y - 6}" font-size="13.5" fill="{C["fg"]}" '
            f'class="b" text-anchor="end">{v}</text>'
        )
    if extra:
        parts.append(
            f'<text x="{PANEL_W - PAD}" y="{y + 14}" font-size="11" fill="{C["muted"]}" '
            f'text-anchor="end">{esc(t["more"].format(n=extra))}</text>'
        )

    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> None:
    global C
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", required=True)
    ap.add_argument("--langs", nargs="+", choices=sorted(L10N), default=["zh", "en", "ja", "fr"])
    ap.add_argument("--themes", nargs="+", choices=sorted(THEMES), default=["dark", "light"])
    ap.add_argument("--title", help="override the panel title")
    ap.add_argument("--top", type=int, default=TOP_N)
    ap.add_argument("--outdir", default="assets")
    ap.add_argument("--basename", default="stats")
    args = ap.parse_args()

    rows = collect(args.user)  # fetch once, render every variant
    for lang in args.langs:
        if args.title:
            L10N[lang]["title"] = args.title
        for theme in args.themes:
            C = THEMES[theme]
            path = out_path(args.outdir, args.basename, lang, theme)
            with open(path, "w", encoding="utf-8") as f:
                f.write(render(rows, lang, args.top))
            print(f"wrote {path} ({theme}, {len(rows)} repos)")


if __name__ == "__main__":
    main()
