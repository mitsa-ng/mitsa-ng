# Hi, I'm Nati (`mitsa-ng`)

Student developer from Taiwan. TypeScript full-stack by day, Rust tinkerer by
night. Currently going deep on **open-source infrastructure**: virtualization,
backup mechanics, and WAF rule evaluation. I learn systems by rebuilding their
guts in small, dependency-free code.

## Infrastructure toolkit

| Project | What it does | Stack |
|---|---|---|
| [chunk-vault](https://github.com/mitsa-ng/chunk-vault) | Content-defined chunking backup vault: gear-hash CDC, SHA-256 chunk store, verify, GC (Proxmox BS style dedup, from the inside) | Python, stdlib only |
| [pve-audit](https://github.com/mitsa-ng/pve-audit) | Proxmox VE backup coverage auditor: flags guests no enabled vzdump job protects; real PVE API tokens and `/api2/json` | Python, stdlib only |
| [crs-check](https://github.com/mitsa-ng/crs-check) | Offline ModSecurity SecRule parser and evaluator: see which OWASP CRS-style rules fire on a request, without a web server | TypeScript, zero deps |

Every repo ships with tests that run without network access.

## Also built: healthcare interoperability toolkit

Three zero-dependency FHIR tools, written while evaluating the medical-standards
path: [fhir-lens](https://github.com/mitsa-ng/fhir-lens) (R4 validator + client),
[smart-launch](https://github.com/mitsa-ng/smart-launch) (SMART on FHIR with
PKCE), [hl7v2-fhir-bridge](https://github.com/mitsa-ng/hl7v2-fhir-bridge)
(HL7 v2 to R4 converter).

## Systems & side quests

- **surf**: a browser built from scratch in Rust
- **nanollm**: minimal C++17 LLM inference runtime, runs Qwen2.5 end to end
- **pdiary**: privacy-first voice diary, on-device transcription with llama.cpp
- **mcgit**: Minecraft server world sync with distributed locking

## Currently learning

Proxmox VE administration, ZFS, backup strategy (3-2-1, pull-mode isolation),
ModSecurity/OWASP CRS tuning, and Debian server hygiene.

## Contact

- GitHub: you are here
- [Personal site](https://mitsa.dpdns.org/zh-TW)
