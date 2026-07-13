<!-- ============================================ -->
<!--  GitHub Profile README for mitsa-ng (Nati)   -->
<!--  日本語版 · メインは README.md（English）      -->
<!-- ============================================ -->

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=24&pause=1200&color=58A6FF&center=true&vCenter=true&width=650&lines=hi%2C+I%27m+Nati+%F0%9F%91%8B;I+build+full-stack+systems+%26+local-first+AI;TypeScript+%2F+Python+%2F+Rust+%2F+Dart;...and+the+occasional+multiplayer+game" alt="intro" />

<img src="https://komarev.com/ghpvc/?username=mitsa-ng&style=flat-square&color=58a6ff&label=visitors" alt="visitors" />

[繁體中文](./README.md) · [English](./README.en.md) · **日本語** · [Français](./README.fr.md)

</div>

<br/>

## `~$ whoami`

```typescript
const nati = {
  focus: ["フルスタックシステム", "オンデバイス AI", "マルチプレイヤーゲーム"],

  stack: {
    frontend: ["TypeScript", "Next.js", "React", "Vue"],
    backend:  ["Python", "Node.js", "Rust"],
    mobile:   ["Flutter", "Kotlin"],
    ai:       ["whisper.cpp", "llama.cpp", "OCR + LLM pipelines"],
    infra:    ["Docker", "Cloudflare Workers", "Vercel", "Neon Postgres"],
  },

  beliefs: [
    "プライバシーは設定項目ではなく、機能そのもの",
    "クラウドが必要なら、まず「なぜ」を問う",
    "まず出荷、それから磨く",
  ],
} satisfies Developer;
```

<br/>

## `~$ ls ~/projects --featured`

|     | プロジェクト | なにをするもの？ | スタック |
| :-: | :----------- | :--------------- | :------- |
| 🔐 | **[pdiary](https://github.com/mitsa-ng/pdiary)** | プライバシー最優先の AI 音声日記——話すだけで、オンデバイスの Whisper が文字起こしし、ローカル LLM が文体を書き換え、AES-256-GCM で暗号化保存。**データは端末から一切外に出ない設計。** | `Flutter` `whisper.cpp` `llama.cpp` |
| ⛏️ | **[mcgit](https://github.com/mitsa-ng/mcgit)** | `git pull` / `git push`——ただし対象は Minecraft のワールド。分散ロックでホストを同時に 1 人へ限定し、バージョン履歴は Postgres に保存。 | `Python` `Neon Postgres` |
| 🧩 | **[block-puzzle](https://github.com/mitsa-ng/block-puzzle)** | リプレイ機能付きのマルチプレイヤー・ブロックパズル PWA——ルームは Cloudflare Durable Objects 上で動作し、オフラインでもプレイ可能。 | `JavaScript` `Cloudflare Workers` `PWA` |
| ✍️ | **[Project-Eat](https://github.com/mitsa-ng/Project-Eat)** | 英作文添削ツール——カメラ／スキャン入力 → OCR → NLP と LLM のハイブリッドパイプラインで自動添削。 | `Python` `OCR` `LLM` |
| 🖥️ | **[website](https://github.com/mitsa-ng/website)** | ただの個人サイトではなく、三層システム：Next.js の公開サイト＋Electron の管理コンソール＋バックグラウンドのレンダリングサービス。 | `Next.js` `Electron` `TypeScript` |
| 📊 | **[OmniBoard](https://github.com/mitsa-ng/OmniBoard)** | フルスタックのボードアプリ——フロントは TypeScript、バックは Rust、完全コンテナ化。→ [live](https://omniboard-app.vercel.app) | `TypeScript` `Rust` `Docker` |

<details>
<summary><b><code>~$ ls ~/projects --all</code></b> &nbsp;·&nbsp; ラボにはまだ実験がいろいろ</summary>
<br/>

- 🤖 **[omniflow](https://github.com/mitsa-ng/omniflow)** — クロスプラットフォーム自動化：Web＋ネイティブ Android（Capacitor/Kotlin）＋OAuth リレー＋Gemini API
- 🀄 **[six-people-majon](https://github.com/mitsa-ng/six-people-majon)** — 6 人リモート同期の台湾麻雀：ホスト権威の状態同期、完全なルールエンジン（チー／ポン／カン／和了）
- ♟️ **[chess](https://github.com/mitsa-ng/chess)** — ブラウザで遊べるチェス → [live](https://mitchess.vercel.app)
- 🅿️ **[parkwhere](https://github.com/mitsa-ng/parkwhere)** — Next.js 製の駐車スペース検索ツール → [live](https://parkhuh.vercel.app)
- 🎛️ **[ichisys](https://github.com/mitsa-ng/ichisys)** — Vue＋Python のフルスタックアプリ。Web *と* Electron デスクトップの両方で提供、Docker で開発／本番環境を統一 → [live](https://ichisys.vercel.app)
- 🎵 **[maiplayerprofile](https://github.com/mitsa-ng/maiplayerprofile)** — maimai プレイヤーカード生成ツール。Hugging Face Spaces（Gradio）にデプロイ
- 📺 **[yt-TV](https://github.com/mitsa-ng/yt-TV)** — YouTube TV（Leanback）を Electron デスクトップクライアントに
- 📝 **[MarkDownEditor](https://github.com/mitsa-ng/MarkDownEditor)** — Windows 向けの軽量 Markdown エディタ
- 📼 **[anime1ArchiveTool](https://github.com/mitsa-ng/anime1ArchiveTool)** — ffmpeg 同梱の CLI アーカイブツール
- 🗂️ **[robocopyTool](https://github.com/mitsa-ng/robocopyTool)** — robocopy を Python でラップしたファイル同期ツール

</details>

<br/>

## `~$ cat stack.txt`

**言語**

<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" /> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white" alt="Dart" /> <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" /> <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />

**フレームワーク & アプリ**

<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js" /> <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React" /> <img src="https://img.shields.io/badge/Vue.js-35495E?style=flat-square&logo=vuedotjs&logoColor=4FC08D" alt="Vue" /> <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" alt="Flutter" /> <img src="https://img.shields.io/badge/Electron-2B2E3A?style=flat-square&logo=electron&logoColor=9FEAF9" alt="Electron" /> <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind" /> <img src="https://img.shields.io/badge/Capacitor-119EFF?style=flat-square&logo=capacitor&logoColor=white" alt="Capacitor" />

**AI——できる限りオンデバイスで**

<img src="https://img.shields.io/badge/whisper.cpp-4A154B?style=flat-square" alt="whisper.cpp" /> <img src="https://img.shields.io/badge/llama.cpp-8A2BE2?style=flat-square" alt="llama.cpp" /> <img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini" /> <img src="https://img.shields.io/badge/AES--256--GCM-DC143C?style=flat-square" alt="AES-256-GCM" />

**インフラ & デプロイ**

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

`~$ echo "最後までスクロールしてくれてありがとう——このページのソースもリポジトリです"`

<!-- Add your links here when ready:
[![X](https://img.shields.io/badge/@handle-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/handle)
[![Email](https://img.shields.io/badge/email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:you@example.com)
-->

</div>
