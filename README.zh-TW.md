<!-- ============================================ -->
<!--  GitHub Profile README for mitsa-ng (Nati)   -->
<!--  繁體中文版 · 主檔為 README.md（English）      -->
<!-- ============================================ -->

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=24&pause=1200&color=58A6FF&center=true&vCenter=true&width=650&lines=hi%2C+I%27m+Nati+%F0%9F%91%8B;I+build+full-stack+systems+%26+local-first+AI;TypeScript+%2F+Python+%2F+Rust+%2F+Dart;...and+the+occasional+multiplayer+game" alt="intro" />

<img src="https://komarev.com/ghpvc/?username=mitsa-ng&style=flat-square&color=58a6ff&label=visitors" alt="visitors" />

[English](./README.md) · **繁體中文** · [日本語](./README.ja.md) · [Français](./README.fr.md)

</div>

<br/>

## `~$ whoami`

```typescript
const nati = {
  focus: ["全端系統", "裝置端 AI", "多人連線遊戲"],

  stack: {
    frontend: ["TypeScript", "Next.js", "React", "Vue"],
    backend:  ["Python", "Node.js", "Rust"],
    mobile:   ["Flutter", "Kotlin"],
    ai:       ["whisper.cpp", "llama.cpp", "OCR + LLM pipelines"],
    infra:    ["Docker", "Cloudflare Workers", "Vercel", "Neon Postgres"],
  },

  beliefs: [
    "隱私是功能，不是設定選項",
    "要上雲之前，先問一句為什麼",
    "先出貨，再打磨",
  ],
} satisfies Developer;
```

<br/>

## `~$ ls ~/projects --featured`

|     | 專案 | 做什麼 | 技術 |
| :-: | :--- | :----- | :--- |
| 🔐 | **[pdiary](https://github.com/mitsa-ng/pdiary)** | 隱私優先的 AI 語音日記——開口說話，裝置端 Whisper 轉錄，本地 LLM 重寫語氣，AES-256-GCM 加密儲存。**內容永遠不離開你的裝置。** | `Flutter` `whisper.cpp` `llama.cpp` |
| ⛏️ | **[mcgit](https://github.com/mitsa-ng/mcgit)** | `git pull` / `git push`——但對象是 Minecraft 世界存檔。分散式鎖保證同一時間只有一位服主；版本歷史存在 Postgres。 | `Python` `Neon Postgres` |
| 🧩 | **[block-puzzle](https://github.com/mitsa-ng/block-puzzle)** | 多人方塊消除 PWA，支援對戰回放——房間跑在 Cloudflare Durable Objects 上，離線也能玩。 | `JavaScript` `Cloudflare Workers` `PWA` |
| ✍️ | **[Project-Eat](https://github.com/mitsa-ng/Project-Eat)** | 作文批改工具——相機／掃描輸入 → OCR → NLP＋LLM 混合管線，自動批改英文作文。 | `Python` `OCR` `LLM` |
| 🖥️ | **[website](https://github.com/mitsa-ng/website)** | 不只是個人網站——三層系統：Next.js 公開網站＋Electron 管理後台＋背景渲染服務。 | `Next.js` `Electron` `TypeScript` |
| 📊 | **[OmniBoard](https://github.com/mitsa-ng/OmniBoard)** | 全端看板應用——TypeScript 前端、Rust 後端、完整容器化。→ [live](https://omniboard-app.vercel.app) | `TypeScript` `Rust` `Docker` |

<details>
<summary><b><code>~$ ls ~/projects --all</code></b> &nbsp;·&nbsp; 實驗室裡還有更多</summary>
<br/>

- 🤖 **[omniflow](https://github.com/mitsa-ng/omniflow)** — 跨平台工作流自動化：Web＋原生 Android（Capacitor/Kotlin）＋OAuth 中繼＋Gemini API
- 🀄 **[six-people-majon](https://github.com/mitsa-ng/six-people-majon)** — 六人遠端連線台灣麻將：房主權威狀態同步，完整規則引擎（吃碰槓胡）
- ♟️ **[chess](https://github.com/mitsa-ng/chess)** — 瀏覽器就能玩的西洋棋 → [live](https://mitchess.vercel.app)
- 🅿️ **[parkwhere](https://github.com/mitsa-ng/parkwhere)** — 用 Next.js 打造的停車位查詢工具 → [live](https://parkhuh.vercel.app)
- 🎛️ **[ichisys](https://github.com/mitsa-ng/ichisys)** — Vue＋Python 全端應用，同時以 Web *和* Electron 桌面版出貨，Docker 開發／正式環境一致 → [live](https://ichisys.vercel.app)
- 🎵 **[maiplayerprofile](https://github.com/mitsa-ng/maiplayerprofile)** — maimai 玩家卡片產生器，部署在 Hugging Face Spaces（Gradio）
- 📺 **[yt-TV](https://github.com/mitsa-ng/yt-TV)** — 把 YouTube TV（Leanback）做成 Electron 桌面客戶端
- 📝 **[MarkDownEditor](https://github.com/mitsa-ng/MarkDownEditor)** — Windows 上的輕量 Markdown 編輯器
- 📼 **[anime1ArchiveTool](https://github.com/mitsa-ng/anime1ArchiveTool)** — 內建 ffmpeg 的 CLI 存檔工具
- 🗂️ **[robocopyTool](https://github.com/mitsa-ng/robocopyTool)** — robocopy 檔案同步的 Python 包裝

</details>

<br/>

## `~$ cat stack.txt`

**語言**

<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" /> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white" alt="Dart" /> <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" /> <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />

**框架與應用**

<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js" /> <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React" /> <img src="https://img.shields.io/badge/Vue.js-35495E?style=flat-square&logo=vuedotjs&logoColor=4FC08D" alt="Vue" /> <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" alt="Flutter" /> <img src="https://img.shields.io/badge/Electron-2B2E3A?style=flat-square&logo=electron&logoColor=9FEAF9" alt="Electron" /> <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind" /> <img src="https://img.shields.io/badge/Capacitor-119EFF?style=flat-square&logo=capacitor&logoColor=white" alt="Capacitor" />

**AI——能在裝置端跑，就在裝置端跑**

<img src="https://img.shields.io/badge/whisper.cpp-4A154B?style=flat-square" alt="whisper.cpp" /> <img src="https://img.shields.io/badge/llama.cpp-8A2BE2?style=flat-square" alt="llama.cpp" /> <img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini" /> <img src="https://img.shields.io/badge/AES--256--GCM-DC143C?style=flat-square" alt="AES-256-GCM" />

**基礎設施與部署**

<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" /> <img src="https://img.shields.io/badge/Cloudflare_Workers-F38020?style=flat-square&logo=cloudflare&logoColor=white" alt="Cloudflare Workers" /> <img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white" alt="Vercel" /> <img src="https://img.shields.io/badge/Netlify-00C7B7?style=flat-square&logo=netlify&logoColor=white" alt="Netlify" /> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" /> <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face" />

<br/>

## `~$ git log --stat`

<div align="center">

<img height="165" src="https://streak-stats.demolab.com?user=mitsa-ng&hide_border=true&background=0D1117&ring=58A6FF&fire=58A6FF&currStreakNum=C9D1D9&sideNums=C9D1D9&currStreakLabel=58A6FF&sideLabels=C9D1D9&dates=8B949E&stroke=30363D" alt="GitHub streak" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=mitsa-ng&layout=compact&langs_count=8&hide=html,css,shell&theme=github_dark&hide_border=true&bg_color=0d1117" alt="Top languages" />

<img width="92%" src="https://github-readme-activity-graph.vercel.app/graph?username=mitsa-ng&theme=github-compact&hide_border=true&bg_color=0d1117&color=58a6ff&line=58a6ff&point=c9d1d9" alt="Contribution graph" />

</div>

<br/>

<div align="center">

`~$ echo "感謝滑到這裡——這個頁面本身也是一個 repo"`

<!-- Add your links here when ready:
[![X](https://img.shields.io/badge/@handle-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/handle)
[![Email](https://img.shields.io/badge/email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:you@example.com)
-->

</div>
