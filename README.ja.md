<!-- ============================================ -->
<!--  GitHub Profile README for mitsa-ng (Nati)   -->
<!--  日本語版 · デフォルトは README.md（繁体字）    -->
<!-- ============================================ -->

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1f6feb,100:58a6ff&height=210&section=header&text=Nati&fontSize=64&fontColor=ffffff&animation=fadeIn&fontAlignY=32&desc=Full-stack%20%C2%B7%20On-device%20AI%20%C2%B7%20Multiplayer%20Games&descSize=16&descAlignY=52" alt="banner" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=24&pause=1200&color=58A6FF&center=true&vCenter=true&width=650&lines=hi%2C+I%27m+Nati+%F0%9F%91%8B;I+build+full-stack+systems+%26+local-first+AI;TypeScript+%2F+Python+%2F+Rust+%2F+Dart;...and+the+occasional+multiplayer+game" alt="intro" />

<img src="https://komarev.com/ghpvc/?username=mitsa-ng&style=flat-square&color=58a6ff&label=visitors" alt="visitors" />

[繁體中文](./README.md) · [English](./README.en.md) · **日本語** · [Français](./README.fr.md)

</div>

<br/>

## 👋 わたしについて

- 🔭 関心領域は **フルスタックシステム**、**オンデバイス AI**、**マルチプレイヤーゲーム**
- 🔐 **プライバシーは設定項目ではなく、機能そのもの**——端末で動くものは、クラウドに送らない
- 🚢 モットー：**まず出荷、それから磨く**——公開リポジトリ 18 件、うち 6 件はライブデモつき
- 💬 好きな話題：オンデバイス AI、プライバシーエンジニアリング、マルチプレイヤー同期、フルスタック設計

## 🧭 いま取り組んでいること

- 🔬 **pdiary** の仕上げ——ローカル LLM による文体書き換えパイプライン（llama.cpp）を日常使いレベルへ
- 🦀 **Rust バックエンド**（OmniBoard）と**分散状態同期**（mcgit、block-puzzle）を深掘り中
- 🌱 継続テーマ：**オンデバイス AI の実用化**——量子化、Metal アクセラレーション、プライバシー最優先の設計

<br/>

## 🚀 注目プロジェクト

### 🔐 [pdiary](https://github.com/mitsa-ng/pdiary)｜プライバシー最優先の AI 音声日記

`Flutter` `whisper.cpp` `llama.cpp` `AES-256-GCM` — iOS / Android / macOS

> 話すだけ——オンデバイスの Whisper が文字起こしし、ローカル LLM が文体を書き換え、暗号化してから保存。
> **データは最初から最後まで端末の外に出ない。**

### ⛏️ [mcgit](https://github.com/mitsa-ng/mcgit)｜Minecraft ワールドのバージョン管理

`Python` `Neon Postgres` `分散ロック`

> `git pull` / `git push` の体験を Minecraft サーバーのセーブデータに——
> 分散ロックでホストを同時 1 人に限定、履歴は Postgres に保存、セーブデータの上書き事故を根絶。

### 🧩 [block-puzzle](https://github.com/mitsa-ng/block-puzzle)｜マルチプレイヤー・ブロックパズル PWA

`JavaScript` `Cloudflare Durable Objects` `PWA`

> ルームサービスは Cloudflare Durable Objects 上で動作——対戦、リプレイ、オフラインプレイに対応。

### ✍️ [Project-Eat](https://github.com/mitsa-ng/Project-Eat)｜AI 英作文添削

`Python` `OCR` `LLM`

> カメラ／スキャン入力 → OCR → NLP と LLM のハイブリッドパイプラインで自動添削——先生の時間を取り戻す教育ツール。

### 🖥️ [website](https://github.com/mitsa-ng/website)｜三層構成の個人サイトシステム

`Next.js` `Electron` `TypeScript`

> ただの個人サイトではなく：Next.js の公開サイト＋Electron の管理コンソール＋バックグラウンドのレンダリングサービス。

### 📊 [OmniBoard](https://github.com/mitsa-ng/OmniBoard)｜TypeScript＋Rust のフルスタックボード · [🔗 live](https://omniboard-app.vercel.app)

`TypeScript` `Rust` `Docker`

> フロントは TypeScript、バックは Rust、完全コンテナ化——docker-compose ひとつで起動。

<details>
<summary><b>📦 ラボの実験いろいろ（クリックで展開）</b></summary>
<br/>

- 🤖 **[omniflow](https://github.com/mitsa-ng/omniflow)** — クロスプラットフォーム自動化：Web＋ネイティブ Android（Capacitor/Kotlin）＋OAuth リレー＋Gemini API
- 🀄 **[six-people-majon](https://github.com/mitsa-ng/six-people-majon)** — 6 人リモート同期の台湾麻雀：ホスト権威の状態同期、完全なルールエンジン（チー／ポン／カン／和了）
- ♟️ **[chess](https://github.com/mitsa-ng/chess)** — ブラウザで遊べるチェス → [live](https://mitchess.vercel.app)
- 🅿️ **[parkwhere](https://github.com/mitsa-ng/parkwhere)** — Next.js 製の駐車スペース検索ツール → [live](https://parkhuh.vercel.app)
- 🎛️ **[ichisys](https://github.com/mitsa-ng/ichisys)** — Vue＋Python のフルスタックアプリ。Web *と* Electron デスクトップの両方で提供 → [live](https://ichisys.vercel.app)
- 🎵 **[maiplayerprofile](https://github.com/mitsa-ng/maiplayerprofile)** — maimai プレイヤーカード生成ツール。Hugging Face Spaces（Gradio）にデプロイ
- 📺 **[yt-TV](https://github.com/mitsa-ng/yt-TV)** — YouTube TV（Leanback）を Electron デスクトップクライアントに
- 📝 **[MarkDownEditor](https://github.com/mitsa-ng/MarkDownEditor)** — Windows 向けの軽量 Markdown エディタ
- 📼 **[anime1ArchiveTool](https://github.com/mitsa-ng/anime1ArchiveTool)** — ffmpeg 同梱の CLI アーカイブツール
- 🗂️ **[robocopyTool](https://github.com/mitsa-ng/robocopyTool)** — robocopy を Python でラップしたファイル同期ツール

</details>

<br/>

## 🛠️ 技術スタック

<div align="center">

**言語**

<img src="https://skillicons.dev/icons?i=ts,js,py,dart,rust,kotlin&theme=dark" alt="languages" />

**フレームワーク & アプリ**

<img src="https://skillicons.dev/icons?i=nextjs,react,vue,flutter,electron,tailwind,nodejs&theme=dark" alt="frameworks" />

**オンデバイス AI & セキュリティ**

<img src="https://img.shields.io/badge/whisper.cpp-4A154B?style=for-the-badge" alt="whisper.cpp" /> <img src="https://img.shields.io/badge/llama.cpp-8A2BE2?style=for-the-badge" alt="llama.cpp" /> <img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini" /> <img src="https://img.shields.io/badge/AES--256--GCM-DC143C?style=for-the-badge" alt="AES-256-GCM" />

**インフラ & デプロイ**

<img src="https://skillicons.dev/icons?i=docker,cloudflare,vercel,netlify,postgres&theme=dark" alt="infra" />

</div>

<br/>

## 📊 GitHub 統計

<div align="center">

<img height="165" src="https://streak-stats.demolab.com?user=mitsa-ng&hide_border=true&background=0D1117&ring=58A6FF&fire=58A6FF&currStreakNum=C9D1D9&sideNums=C9D1D9&currStreakLabel=58A6FF&sideLabels=C9D1D9&dates=8B949E&stroke=30363D" alt="GitHub streak" />
<img height="165" src="./assets/top-langs.svg" alt="Top languages" />

<img width="92%" src="https://github-readme-activity-graph.vercel.app/graph?username=mitsa-ng&theme=github-compact&hide_border=true&bg_color=0d1117&color=58a6ff&line=58a6ff&point=c9d1d9" alt="Contribution graph" />

</div>

<br/>

## 🤝 オープンソース & コンタクト

- ✅ どのリポジトリも **Issue / PR 歓迎**——バグ報告もアイデアも、気軽にどうぞ。必ず目を通します
- 🧑‍💻 特に **pdiary**（オンデバイス AI）と **mcgit**（分散ツール）でのコラボ大歓迎
- 💼 **お仕事のご相談・コラボのお誘い**も受け付けています——リモート歓迎

<div align="center">
<br/>

[![Email](https://img.shields.io/badge/Email-catchatapp6%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:catchatapp6@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-mitsa--ng-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mitsa-ng)

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1f6feb,100:58a6ff&height=110&section=footer" alt="footer" />

</div>
