# こんにちは、Nati（`mitsa-ng`）です

[繁體中文](./README.md) · [English](./README.en.md) · **日本語** · [Français](./README.fr.md)

台湾の学生開発者です。日中は TypeScript フルスタック、夜は Rust いじり。
現在は**オープンソースインフラ**（仮想化、バックアップ機構、WAF ルール評価）
を深掘りしています。システムの内部構造を、依存ゼロの小さなコードで
再実装して学ぶのがスタイルです。

## インフラツールキット

| プロジェクト | 何をするか | 技術 |
|---|---|---|
| [chunk-vault](https://github.com/mitsa-ng/chunk-vault) | コンテンツ定義チャンキングのバックアップボールト。gear-hash CDC、SHA-256 チャンクストア、検証、GC（Proxmox BS 式重複排除を内側から実装） | Python 標準ライブラリのみ |
| [pve-audit](https://github.com/mitsa-ng/pve-audit) | Proxmox VE バックアップ網羅監査。有効な vzdump ジョブに保護されていないゲストを検出。実際の PVE API トークンと `/api2/json` に対応 | Python 標準ライブラリのみ |
| [crs-check](https://github.com/mitsa-ng/crs-check) | ModSecurity SecRule のオフラインパーサと評価エンジン。Web サーバなしで OWASP CRS 系ルールの発火を確認 | TypeScript、依存ゼロ |

どのリポジトリも、ネットワーク不要で実行できるテストを同梱しています。

## 別枠：医療相互運用ツールキット

依存ゼロの FHIR ツール 3 点（医療標準の道を検討していた時期に作成）：
[fhir-lens](https://github.com/mitsa-ng/fhir-lens)（R4 バリデータ＋クライアント）、
[smart-launch](https://github.com/mitsa-ng/smart-launch)（PKCE 付き SMART on FHIR）、
[hl7v2-fhir-bridge](https://github.com/mitsa-ng/hl7v2-fhir-bridge)（HL7 v2 → R4 コンバータ）。

## システムと趣味プロジェクト

- **surf**: Rust でゼロから作るブラウザ
- **nanollm**: C++17 の最小 LLM 推理ランタイム。Qwen2.5 をエンドツーエンドで実行
- **pdiary**: プライバシー優先の音声日記。llama.cpp でオンデバイス書き起こし
- **mcgit**: 分散ロック付き Minecraft ワールド同期

## 現在学んでいること

Proxmox VE 管理、ZFS、バックアップ戦略（3-2-1、プル型分離）、
ModSecurity/OWASP CRS チューニング、Debian サーバ運用。

## 連絡

- GitHub：今いるところ
- [個人サイト](https://mitsa.dpdns.org/zh-TW)

**採用ご担当者様へ**：[履歴書（PDF・繁体字中国語）](./resume.pdf)
オープンソースインフラエンジニア（仮想化／バックアップ／セキュリティ）。
学生で、インターンまたは正社員としての面談が可能です
