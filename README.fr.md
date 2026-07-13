<!-- ============================================ -->
<!--  GitHub Profile README for mitsa-ng (Nati)   -->
<!--  Version française · principal : README.md   -->
<!-- ============================================ -->

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=24&pause=1200&color=58A6FF&center=true&vCenter=true&width=650&lines=hi%2C+I%27m+Nati+%F0%9F%91%8B;I+build+full-stack+systems+%26+local-first+AI;TypeScript+%2F+Python+%2F+Rust+%2F+Dart;...and+the+occasional+multiplayer+game" alt="intro" />

<img src="https://komarev.com/ghpvc/?username=mitsa-ng&style=flat-square&color=58a6ff&label=visitors" alt="visitors" />

[English](./README.md) · [繁體中文](./README.zh-TW.md) · [日本語](./README.ja.md) · **Français**

</div>

<br/>

## `~$ whoami`

```typescript
const nati = {
  focus: ["systèmes full-stack", "IA embarquée", "jeux multijoueurs"],

  stack: {
    frontend: ["TypeScript", "Next.js", "React", "Vue"],
    backend:  ["Python", "Node.js", "Rust"],
    mobile:   ["Flutter", "Kotlin"],
    ai:       ["whisper.cpp", "llama.cpp", "OCR + LLM pipelines"],
    infra:    ["Docker", "Cloudflare Workers", "Vercel", "Neon Postgres"],
  },

  beliefs: [
    "la vie privée est une fonctionnalité, pas un réglage",
    "si ça exige le cloud, demander d'abord pourquoi",
    "livrer d'abord, peaufiner ensuite",
  ],
} satisfies Developer;
```

<br/>

## `~$ ls ~/projects --featured`

|     | projet | ce que ça fait | stack |
| :-: | :----- | :------------- | :---- |
| 🔐 | **[pdiary](https://github.com/mitsa-ng/pdiary)** | Journal vocal IA axé sur la confidentialité — parlez, Whisper transcrit sur l'appareil, un LLM local réécrit le ton, le tout chiffré en AES-256-GCM. **Rien ne quitte jamais l'appareil.** | `Flutter` `whisper.cpp` `llama.cpp` |
| ⛏️ | **[mcgit](https://github.com/mitsa-ng/mcgit)** | `git pull` / `git push` — mais pour des mondes Minecraft. Un verrou distribué garantit un seul hôte à la fois ; l'historique des versions vit dans Postgres. | `Python` `Neon Postgres` |
| 🧩 | **[block-puzzle](https://github.com/mitsa-ng/block-puzzle)** | PWA de puzzle multijoueur avec replays — les salons tournent sur Cloudflare Durable Objects, jouable hors ligne. | `JavaScript` `Cloudflare Workers` `PWA` |
| ✍️ | **[Project-Eat](https://github.com/mitsa-ng/Project-Eat)** | Outil d'annotation de rédactions — entrée caméra/scan → OCR → pipeline hybride NLP + LLM qui corrige automatiquement des rédactions en anglais. | `Python` `OCR` `LLM` |
| 🖥️ | **[website](https://github.com/mitsa-ng/website)** | Pas un simple site perso — un système à trois niveaux : site public Next.js + console d'admin Electron + service de rendu en arrière-plan. | `Next.js` `Electron` `TypeScript` |
| 📊 | **[OmniBoard](https://github.com/mitsa-ng/OmniBoard)** | Application de tableaux full-stack — front en TypeScript, back en Rust, entièrement conteneurisée. → [live](https://omniboard-app.vercel.app) | `TypeScript` `Rust` `Docker` |

<details>
<summary><b><code>~$ ls ~/projects --all</code></b> &nbsp;·&nbsp; encore plus d'expériences au labo</summary>
<br/>

- 🤖 **[omniflow](https://github.com/mitsa-ng/omniflow)** — automatisation de flux multiplateforme : Web + Android natif (Capacitor/Kotlin) + relais OAuth + API Gemini
- 🀄 **[six-people-majon](https://github.com/mitsa-ng/six-people-majon)** — mahjong taïwanais à 6 joueurs en synchro distante : état géré par l'hôte, moteur de règles complet (chi/pong/kang/hu)
- ♟️ **[chess](https://github.com/mitsa-ng/chess)** — des échecs dans le navigateur → [live](https://mitchess.vercel.app)
- 🅿️ **[parkwhere](https://github.com/mitsa-ng/parkwhere)** — chercheur de places de parking construit avec Next.js → [live](https://parkhuh.vercel.app)
- 🎛️ **[ichisys](https://github.com/mitsa-ng/ichisys)** — appli full-stack Vue + Python, livrée en Web *et* en desktop Electron, parité dev/prod via Docker → [live](https://ichisys.vercel.app)
- 🎵 **[maiplayerprofile](https://github.com/mitsa-ng/maiplayerprofile)** — générateur de cartes de joueur maimai, déployé sur Hugging Face Spaces (Gradio)
- 📺 **[yt-TV](https://github.com/mitsa-ng/yt-TV)** — YouTube TV (Leanback) en client desktop Electron
- 📝 **[MarkDownEditor](https://github.com/mitsa-ng/MarkDownEditor)** — éditeur Markdown léger pour Windows
- 📼 **[anime1ArchiveTool](https://github.com/mitsa-ng/anime1ArchiveTool)** — archiveur CLI avec ffmpeg embarqué
- 🗂️ **[robocopyTool](https://github.com/mitsa-ng/robocopyTool)** — wrapper Python autour de robocopy pour la synchro de fichiers

</details>

<br/>

## `~$ cat stack.txt`

**langages**

<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" /> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white" alt="Dart" /> <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" /> <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />

**frameworks & applications**

<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js" /> <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React" /> <img src="https://img.shields.io/badge/Vue.js-35495E?style=flat-square&logo=vuedotjs&logoColor=4FC08D" alt="Vue" /> <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" alt="Flutter" /> <img src="https://img.shields.io/badge/Electron-2B2E3A?style=flat-square&logo=electron&logoColor=9FEAF9" alt="Electron" /> <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind" /> <img src="https://img.shields.io/badge/Capacitor-119EFF?style=flat-square&logo=capacitor&logoColor=white" alt="Capacitor" />

**ia — embarquée dès que possible**

<img src="https://img.shields.io/badge/whisper.cpp-4A154B?style=flat-square" alt="whisper.cpp" /> <img src="https://img.shields.io/badge/llama.cpp-8A2BE2?style=flat-square" alt="llama.cpp" /> <img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini" /> <img src="https://img.shields.io/badge/AES--256--GCM-DC143C?style=flat-square" alt="AES-256-GCM" />

**infra & déploiement**

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

`~$ echo "merci d'avoir scrollé — la source de cette page est aussi un dépôt"`

<!-- Add your links here when ready:
[![X](https://img.shields.io/badge/@handle-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/handle)
[![Email](https://img.shields.io/badge/email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:you@example.com)
-->

</div>
