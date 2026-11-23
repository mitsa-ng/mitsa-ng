#!/usr/bin/env python3
"""Generate the "recent pull requests" SVG panel for the profile README.

Fetches the user's most recently updated PRs from the GitHub Search API and
renders an SVG matching the profile's theme (dark + light variants).
Stdlib only; meant to run from .github/workflows/recent-prs.yml but works
locally with GITHUB_TOKEN (or plain anonymous, rate-limited) access.
"""

import argparse
import json
import os
import sys
import unicodedata
import urllib.parse
import urllib.request
from datetime import datetime, timezone

THEMES = {
    "dark": dict(
        bg="#0d1117", border="#30363d", accent="#58a6ff", fg="#c9d1d9",
        muted="#8b949e", sep="#21262d", merged="#a371f7", opened="#3fb950",
        closed="#f85149",
    ),
    "light": dict(
        bg="#f6f8fa", border="#d0d7de", accent="#0969da", fg="#1f2328",
        muted="#656d76", sep="#d8dee4", merged="#8250df", opened="#1a7f37",
        closed="#cf222e",
    ),
}
C = THEMES["dark"]

PANEL_W = 840
PAD = 26
ROW_H = 47
LIST_Y = 82
FONT = "-apple-system, 'Helvetica Neue', 'PingFang TC', 'Hiragino Sans', Arial, sans-serif"

# per-language strings: panel title, state labels, relative time
L10N = {
    "zh": {
        "title": "最近 PR",
        "merged": "已合併",
        "open": "開放中",
        "closed": "已關閉",
        "updated": "最後更新",
        "empty": "還沒有 PR",
        "rel": [("分鐘前", "分鐘"), ("小時前", "小時"), ("天前", "天")],
    },
    "en": {
        "title": "Recent Pull Requests",
        "merged": "Merged",
        "open": "Open",
        "closed": "Closed",
        "updated": "updated",
        "empty": "No pull requests yet",
        "rel": [("m ago", "m"), ("h ago", "h"), ("d ago", "d")],
    },
    "ja": {
        "title": "最近のプルリクエスト",
        "merged": "マージ済み",
        "open": "オープン",
        "closed": "クローズ",
        "updated": "最終更新",
        "empty": "PR はまだありません",
        "rel": [("分前", "分"), ("時間前", "時間"), ("日前", "日")],
    },
    "fr": {
        "title": "Pull requests récentes",
        "merged": "Fusionnée",
        "open": "Ouverte",
        "closed": "Fermée",
        "updated": "maj",
        "empty": "Aucune pull request",
        "rel": [("min", "min"), ("h", "h"), ("j", "j")],
    },
}


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def text_w(s: str, size: float, bold: bool = False) -> float:
    """Approximate rendered width (CJK-aware); good enough for truncation."""
    w = 0.0
    for ch in s:
        if unicodedata.east_asian_width(ch) in ("W", "F"):
            w += size
        elif ch in "iIljtf.,:;'|!()[]-":
            w += size * 0.32
        elif ch.isupper() or ch.isdigit():
            w += size * 0.62
        else:
            w += size * 0.53
    return w * (1.06 if bold else 1.0)


def fit(s: str, size: float, max_w: float, bold: bool = False) -> str:
    if text_w(s, size, bold) <= max_w:
        return s
    while s and text_w(s + "…", size, bold) > max_w:
        s = s[:-1]
    return s + "…"


def rel_time(dt: datetime, lang: str) -> str:
    units = L10N[lang]["rel"]
    mins = int((datetime.now(timezone.utc) - dt).total_seconds() // 60)
    if mins < 1:
        return {"zh": "剛剛", "ja": "たった今"}.get(lang, "now")
    if mins < 60:
        value, unit = mins, units[0]
    elif mins < 60 * 24:
        value, unit = mins // 60, units[1]
    elif mins < 60 * 24 * 30:
        value, unit = mins // (60 * 24), units[2]
    else:
        return dt.strftime("%Y-%m-%d")
    full, short = unit
    if lang == "fr":
        return f"il y a {value} {short}"
    if lang == "en":
        return f"{value} {full}"
    return f"{value}{full}"  # zh/ja: 3 小時前 / 3時間前


def fetch_prs(user: str, count: int) -> list:
    q = f"is:pr author:{user}"
    url = (
        "https://api.github.com/search/issues?"
        + urllib.parse.urlencode({"q": q, "sort": "updated", "order": "desc", "per_page": count})
    )
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-recent-prs",
    })
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            items = json.load(resp)["items"]
    except Exception as e:  # noqa: BLE001 - surface as a hard failure
        print(f"error: GitHub search API failed: {e}", file=sys.stderr)
        sys.exit(1)

    prs = []
    for it in items:
        merged_at = (it.get("pull_request") or {}).get("merged_at")
        state = "merged" if merged_at else it["state"]
        stamp = merged_at or it["updated_at"]
        parts = it["repository_url"].rstrip("/").rsplit("/", 2)
        owner, repo = parts[-2], parts[-1]
        if owner != user and owner != repo:
            repo = f"{owner}/{repo}"
        prs.append({
            "repo": repo,
            "number": it["number"],
            "title": it["title"],
            "state": state,
            "when": datetime.fromisoformat(stamp.replace("Z", "+00:00")),
        })
    return prs


def render(prs: list, lang: str) -> str:
    t = L10N[lang]
    state_color = {"merged": C["merged"], "open": C["opened"], "closed": C["closed"]}
    state_label = {"merged": t["merged"], "open": t["open"], "closed": t["closed"]}

    rows = len(prs) if prs else 1
    height = LIST_Y + rows * ROW_H + 2
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

    if not prs:
        parts.append(
            f'<text x="{PANEL_W / 2}" y="{LIST_Y + 24}" font-size="13" fill="{C["muted"]}" '
            f'text-anchor="middle">{esc(t["empty"])}</text>'
        )

    for i, pr in enumerate(prs):
        y = LIST_Y + i * ROW_H
        if i:
            parts.append(
                f'<line x1="{PAD}" x2="{PANEL_W - PAD}" y1="{y - 9}" y2="{y - 9}" '
                f'stroke="{C["sep"]}" stroke-width="1"/>'
            )
        c = state_color[pr["state"]]
        # line 1: state dot + label + repo + number, relative time right-aligned
        parts.append(f'<circle cx="{PAD + 7}" cy="{y - 4}" r="4.5" fill="{c}"/>')
        x = PAD + 19
        parts.append(
            f'<text x="{x}" y="{y}" font-size="11" fill="{c}">{esc(state_label[pr["state"]])}</text>'
        )
        x += text_w(state_label[pr["state"]], 11) + 14
        repo_txt = fit(pr["repo"], 12.5, PANEL_W - PAD - x - 140, bold=True)
        parts.append(
            f'<text x="{x}" y="{y}" font-size="12.5" fill="{C["accent"]}" class="b">{esc(repo_txt)}</text>'
        )
        x += text_w(repo_txt, 12.5, True) + 8
        parts.append(
            f'<text x="{x}" y="{y}" font-size="11.5" fill="{C["muted"]}">#{pr["number"]}</text>'
        )
        parts.append(
            f'<text x="{PANEL_W - PAD}" y="{y}" font-size="11" fill="{C["muted"]}" '
            f'text-anchor="end">{esc(rel_time(pr["when"], lang))}</text>'
        )
        # line 2: title
        title = fit(pr["title"], 13.5, PANEL_W - PAD * 2)
        parts.append(
            f'<text x="{PAD}" y="{y + 20}" font-size="13.5" fill="{C["fg"]}">{esc(title)}</text>'
        )

    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def out_path(outdir: str, basename: str, lang: str, theme: str) -> str:
    """assets/recent-prs.svg (zh dark) · .en/.ja/.fr · .light suffix."""
    suffix = "" if lang == "zh" else f".{lang}"
    if theme == "light":
        suffix += ".light"
    return os.path.join(outdir, f"{basename}{suffix}.svg")


def main() -> None:
    global C
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", required=True)
    ap.add_argument("--langs", nargs="+", choices=sorted(L10N), default=["zh", "en", "ja", "fr"])
    ap.add_argument("--themes", nargs="+", choices=sorted(THEMES), default=["dark", "light"])
    ap.add_argument("--title", help="override the panel title")
    ap.add_argument("--max", type=int, default=6)
    ap.add_argument("--outdir", default="assets")
    ap.add_argument("--basename", default="recent-prs")
    args = ap.parse_args()

    prs = fetch_prs(args.user, args.max)  # fetch once, render every variant
    for lang in args.langs:
        if args.title:
            L10N[lang]["title"] = args.title
        for theme in args.themes:
            C = THEMES[theme]
            path = out_path(args.outdir, args.basename, lang, theme)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(render(prs, lang))
            print(f"wrote {path} ({theme}, {len(prs)} PRs)")


if __name__ == "__main__":
    main()
