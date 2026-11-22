# Salut, je suis Nati (`mitsa-ng`)

[繁體中文](./README.md) · [English](./README.en.md) · [日本語](./README.ja.md) · **Français**

Étudiant développeur de Taïwan. TypeScript full-stack le jour, bidouilleur Rust
la nuit. J'approfondis actuellement l'**infrastructure open source** :
virtualisation, mécanismes de sauvegarde et évaluation de règles WAF.
Ma méthode : réimplémenter les mécanismes internes en petit code sans
dépendances.

## Boîte à outils infrastructure

| Projet | Ce que ça fait | Stack |
|---|---|---|
| [chunk-vault](https://github.com/mitsa-ng/chunk-vault) | Coffre de sauvegarde à découpage défini par contenu : CDC par gear-hash, magasin de chunks SHA-256, vérification, GC (la dédup façon Proxmox BS, de l'intérieur) | Python, stdlib uniquement |
| [pve-audit](https://github.com/mitsa-ng/pve-audit) | Auditeur de couverture de sauvegarde Proxmox VE : signale les guests qu'aucune tâche vzdump activée ne protège ; vrais tokens PVE et `/api2/json` | Python, stdlib uniquement |
| [crs-check](https://github.com/mitsa-ng/crs-check) | Parseur et évaluateur hors ligne SecRule ModSecurity : voir quelles règles CRS OWASP se déclenchent, sans serveur web | TypeScript, zéro dépendance |

Chaque dépôt inclut des tests exécutables sans accès réseau.

## Également construit : interopérabilité médicale

Trois outils FHIR sans dépendances (écrits en explorant la voie des standards
médicaux) : [fhir-lens](https://github.com/mitsa-ng/fhir-lens) (validateur +
client R4), [smart-launch](https://github.com/mitsa-ng/smart-launch) (SMART on
FHIR avec PKCE), [hl7v2-fhir-bridge](https://github.com/mitsa-ng/hl7v2-fhir-bridge)
(convertisseur HL7 v2 vers R4).

## Systèmes et projets perso

- **surf** : un navigateur écrit from scratch en Rust
- **nanollm** : runtime d'inférence LLM minimal en C++17, fait tourner Qwen2.5 de bout en bout
- **pdiary** : journal vocal respectueux de la vie privée, transcription sur l'appareil avec llama.cpp
- **mcgit** : synchronisation de mondes Minecraft avec verrou distribué

## En cours d'apprentissage

Administration Proxmox VE, ZFS, stratégies de sauvegarde (3-2-1, isolation
pull), réglage ModSecurity/OWASP CRS, et hygiène des serveurs Debian.

## Contact

- GitHub : vous y êtes
- [Site perso](https://mitsa.dpdns.org/zh-TW)

**Pour les recruteurs** : [CV (PDF, chinois traditionnel)](./resume.pdf)
Ingénieur infrastructure open source (virtualisation / sauvegarde / sécurité),
étudiant, disponible pour un stage ou un entretien en CDI
