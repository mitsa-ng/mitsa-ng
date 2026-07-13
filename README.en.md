<!-- ============================================ -->
<!--  GitHub Profile README for mitsa-ng (Nati)   -->
<!--  English version · default: README.md (繁中) -->
<!-- ============================================ -->

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=24&pause=1200&color=58A6FF&center=true&vCenter=true&width=650&lines=hi%2C+I%27m+Nati+%F0%9F%91%8B;I+build+full-stack+systems+%26+local-first+AI;TypeScript+%2F+Python+%2F+Rust+%2F+Dart;...and+the+occasional+multiplayer+game" alt="intro" />

<img src="https://komarev.com/ghpvc/?username=mitsa-ng&style=flat-square&color=58a6ff&label=visitors" alt="visitors" />

[繁體中文](./README.md) · **English** · [日本語](./README.ja.md) · [Français](./README.fr.md)

</div>

<br/>

## `~$ whoami`

```typescript
const nati = {
  focus: ["full-stack systems", "on-device AI", "multiplayer games"],

  stack: {
    frontend: ["TypeScript", "Next.js", "React", "Vue"],
    backend:  ["Python", "Node.js", "Rust"],
    mobile:   ["Flutter", "Kotlin"],
    ai:       ["whisper.cpp", "llama.cpp", "OCR + LLM pipelines"],
    infra:    ["Docker", "Cloudflare Workers", "Vercel", "Neon Postgres"],
  },

  beliefs: [
    "privacy is a feature, not a setting",
    "if it needs the cloud, ask why first",
    "ship it, then polish it",
  ],
} satisfies Developer;
```

<br/>

## `~$ ls ~/projects --featured`

|     | project | what it does | stack |
| :-: | :------ | :----------- | :---- |
| 🔐 | **[pdiary](https://github.com/mitsa-ng/pdiary)** | Privacy-first AI voice diary — speak, on-device Whisper transcribes, a local LLM rewrites the tone, AES-256-GCM encrypts at rest. **Nothing ever leaves the device.** | `Flutter` `whisper.cpp` `llama.cpp` |
| ⛏️ | **[mcgit](https://github.com/mitsa-ng/mcgit)** | `git pull` / `git push` — but for Minecraft worlds. A distributed lock guarantees one host at a time; version history lives in Postgres. | `Python` `Neon Postgres` |
| 🧩 | **[block-puzzle](https://github.com/mitsa-ng/block-puzzle)** | Multiplayer block-puzzle PWA with match replays — rooms run on Cloudflare Durable Objects, playable offline. | `JavaScript` `Cloudflare Workers` `PWA` |
| ✍️ | **[Project-Eat](https://github.com/mitsa-ng/Project-Eat)** | Essay Annotation Tool — camera/scan input → OCR → hybrid NLP + LLM pipeline that marks English essays automatically. | `Python` `OCR` `LLM` |
| 🖥️ | **[website](https://github.com/mitsa-ng/website)** | Not just a personal site — a three-tier system: Next.js public site + Electron admin console + background render service. | `Next.js` `Electron` `TypeScript` |
| 📊 | **[OmniBoard](https://github.com/mitsa-ng/OmniBoard)** | Full-stack board app — TypeScript front-end, Rust back-end, fully containerised. → [live](https://omniboard-app.vercel.app) | `TypeScript` `Rust` `Docker` |

<details>
<summary><b><code>~$ ls ~/projects --all</code></b> &nbsp;·&nbsp; more experiments in the lab</summary>
<br/>

- 🤖 **[omniflow](https://github.com/mitsa-ng/omniflow)** — cross-platform workflow automation: Web + native Android (Capacitor/Kotlin) + OAuth relay + Gemini API
- 🀄 **[six-people-majon](https://github.com/mitsa-ng/six-people-majon)** — 6-player remote-sync Taiwanese mahjong: host-authoritative state, full rules engine (chi/pong/kang/hu)
- ♟️ **[chess](https://github.com/mitsa-ng/chess)** — chess in the browser → [live](https://mitchess.vercel.app)
- 🅿️ **[parkwhere](https://github.com/mitsa-ng/parkwhere)** — parking-spot finder built with Next.js → [live](https://parkhuh.vercel.app)
- 🎛️ **[ichisys](https://github.com/mitsa-ng/ichisys)** — Vue + Python full-stack app, ships as Web *and* Electron desktop, Docker dev/prod parity → [live](https://ichisys.vercel.app)
- 🎵 **[maiplayerprofile](https://github.com/mitsa-ng/maiplayerprofile)** — maimai player-card generator, deployed on Hugging Face Spaces (Gradio)
- 📺 **[yt-TV](https://github.com/mitsa-ng/yt-TV)** — YouTube TV (Leanback) as an Electron desktop client
- 📝 **[MarkDownEditor](https://github.com/mitsa-ng/MarkDownEditor)** — lightweight Markdown editor for Windows
- 📼 **[anime1ArchiveTool](https://github.com/mitsa-ng/anime1ArchiveTool)** — CLI archiver with bundled ffmpeg
- 🗂️ **[robocopyTool](https://github.com/mitsa-ng/robocopyTool)** — Python wrapper around robocopy for file sync

</details>

<br/>

## `~$ cat stack.txt`

**languages**

<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" /> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white" alt="Dart" /> <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" /> <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />

**frameworks & apps**

<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js" /> <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React" /> <img src="https://img.shields.io/badge/Vue.js-35495E?style=flat-square&logo=vuedotjs&logoColor=4FC08D" alt="Vue" /> <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" alt="Flutter" /> <img src="https://img.shields.io/badge/Electron-2B2E3A?style=flat-square&logo=electron&logoColor=9FEAF9" alt="Electron" /> <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind" /> <img src="https://img.shields.io/badge/Capacitor-119EFF?style=flat-square&logo=capacitor&logoColor=white" alt="Capacitor" />

**ai — runs on-device when it can**

<img src="https://img.shields.io/badge/whisper.cpp-4A154B?style=flat-square" alt="whisper.cpp" /> <img src="https://img.shields.io/badge/llama.cpp-8A2BE2?style=flat-square" alt="llama.cpp" /> <img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini" /> <img src="https://img.shields.io/badge/AES--256--GCM-DC143C?style=flat-square" alt="AES-256-GCM" />

**infra & deploy**

<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" /> <img src="https://img.shields.io/badge/Cloudflare_Workers-F38020?style=flat-square&logo=cloudflare&logoColor=white" alt="Cloudflare Workers" /> <img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white" alt="Vercel" /> <img src="https://img.shields.io/badge/Netlify-00C7B7?style=flat-square&logo=netlify&logoColor=white" alt="Netlify" /> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" /> <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face" />

<br/>

## `~$ git log --stat`

<div align="center">

<img height="165" src="https://streak-stats.demolab.com?user=mitsa-ng&hide_border=true&background=0D1117&ring=58A6FF&fire=58A6FF&currStreakNum=C9D1D9&sideNums=C9D1D9&currStreakLabel=58A6FF&sideLabels=C9D1D9&dates=8B949E&stroke=30363D" alt="GitHub streak" />
<img height="165" src="./assets/top-langs.svg" alt="Top languages" />

<img width="92%" src="https://github-readme-activity-graph.vercel.app/graph?username=mitsa-ng&theme=github-compact&hide_border=true&bg_color=0d1117&color=58a6ff&line=58a6ff&point=c9d1d9" alt="Contribution graph" />

</div>

<br/>

<div align="center">

`~$ echo "thanks for scrolling — the source of this page is a repo too"`

<!-- Add your links here when ready:
[![X](https://img.shields.io/badge/@handle-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/handle)
[![Email](https://img.shields.io/badge/email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:you@example.com)
-->

</div>
