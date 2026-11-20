#!/usr/bin/env python3
"""Regenerate assets/contributions.svg: recent PRs by a user, from the GitHub Search API.

Stdlib only. Reads GH_TOKEN (or GITHUB_TOKEN) from the environment.
Excludes the user's own repositories by default (--include-own to disable).
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
import xml.sax.saxutils as sax

BG, ACCENT, TEXT, MUTED = "#0d1117", "#58a6ff", "#c9d1d9", "#8b949e"
OPEN, MERGED, CLOSED = "#3fb950", "#8957e5", "#f85149"
ROW_H, PAD, W = 26, 16, 720
FONT = "Segoe UI, Helvetica, Arial, sans-serif"


def esc(s: str) -> str:
    return sax.escape(s)


def fetch_prs(user: str, limit: int, include_own: bool, token: str) -> list:
    q = f"is:pr author:{user}"
    if not include_own:
        q += f" -user:{user}"
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
        {"q": q, "sort": "updated", "order": "desc", "per_page": limit}
    )
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "contributions-card",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    rows = []
    for it in data.get("items", []):
        pr = it.get("pull_request", {})
        merged = bool(pr.get("merged_at"))
        state = "merged" if merged else it["state"]
        repo = it["repository_url"].split("repos/")[-1]
        rows.append(
            {
                "repo": repo,
                "number": it["number"],
                "title": it["title"],
                "state": state,
                "date": (it.get("updated_at") or it["created_at"])[:10],
            }
        )
    return rows


def render(rows: list, user: str) -> str:
    n = len(rows)
    h = 58 + n * ROW_H + 10
    out = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" '
        f'viewBox="0 0 {W} {h}" role="img" aria-label="Recent contributions by {esc(user)}">'
    )
    out.append(f'<rect width="{W}" height="{h}" rx="8" fill="{BG}"/>')
    out.append(
        f'<text x="{PAD}" y="34" fill="{ACCENT}" font-family="{FONT}" '
        f'font-size="16" font-weight="600">Recent contributions</text>'
    )
    out.append(
        f'<text x="{W - PAD}" y="34" fill="{MUTED}" font-family="{FONT}" '
        f'font-size="12" text-anchor="end">latest {n} PRs</text>'
    )
    out.append(
        f'<line x1="{PAD}" y1="48" x2="{W - PAD}" y2="48" stroke="#30363d" stroke-width="1"/>'
    )
    colors = {"open": OPEN, "merged": MERGED, "closed": CLOSED}
    for i, r in enumerate(rows):
        y = 58 + i * ROW_H
        cy = y + ROW_H // 2 - 4
        out.append(f'<circle cx="{PAD + 4}" cy="{cy}" r="4" fill="{colors[r["state"]]}"/>')
        repo_label = f'{esc(r["repo"])} #{r["number"]}'
        repo_w = int(len(repo_label) * 6.4) + 10
        date_w = 74
        title_budget = W - PAD - 32 - repo_w - date_w - PAD
        title = r["title"]
        max_chars = max(8, int(title_budget / 6.1))
        if len(title) > max_chars:
            title = title[: max_chars - 1] + "…"
        out.append(
            f'<text x="32" y="{cy + 4}" font-family="{FONT}" font-size="12">'
            f'<tspan fill="{ACCENT}">{esc(repo_label)}</tspan>'
            f'<tspan fill="{TEXT}" dx="10">{esc(title)}</tspan></text>'
        )
        out.append(
            f'<text x="{W - PAD}" y="{cy + 4}" fill="{MUTED}" font-family="{FONT}" '
            f'font-size="11" text-anchor="end">{esc(r["date"])}</text>'
        )
    out.append("</svg>")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=8)
    ap.add_argument("--include-own", action="store_true")
    args = ap.parse_args()

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GH_TOKEN / GITHUB_TOKEN not set", file=sys.stderr)
        return 1
    rows = fetch_prs(args.user, args.limit, args.include_own, token)
    if not rows:
        print("search returned no PRs; keeping the previous card", file=sys.stderr)
        return 1
    svg = render(rows, args.user)
    import xml.dom.minidom

    xml.dom.minidom.parseString(svg)  # fail loudly on malformed output
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(svg + "\n")
    print(f"wrote {args.out}: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
