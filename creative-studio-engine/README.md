# Creative Studio Engine

Sistema de engenharia de prompt para o **Claude Pro (Projects)** que gera, em loop
iterativo, prompts de altíssima fidelidade para:

- **Música** (Suno AI) — style tags + estrutura de letra.
- **Vídeo cinematográfico** (Runway Gen-3, Luma Dream Machine, Kling, etc.) — prompts
  de cena com movimento de câmera, iluminação e lente.

A ideia central é um **Loop de Refinamento Iterativo**: um conjunto de sub-personas
dentro de uma única conversa do Claude gera o conceito, gera o prompt de áudio, gera
o prompt de vídeo, e por fim **critica a coerência entre os dois** (tempo/BPM vs.
movimento de câmera, humor vs. paleta de cores) — refinando ambos antes de entregar o
resultado final.

## Estrutura desta pasta

```
creative-studio-engine/
├── README.md                          este arquivo
├── project-instructions.md            cole em "Project Instructions" no Claude
├── knowledge/                         suba estes arquivos em "Project Knowledge"
│   ├── suno-style-dictionary.md       gêneros, tags de produção, tags de estrutura
│   ├── camera-dictionary.md           movimentos de câmera (pan, tilt, dolly...)
│   ├── lens-reference.md              lentes, distância focal, profundidade de campo
│   └── lighting-glossary.md           iluminação (golden hour, rim light, neon...)
├── projects/emrys/                    implementação específica para o artista EMRYS
└── automation/                        orquestrador real (API da Claude) do loop
                                        de agentes — CEO + 7 especialistas, ver
                                        automation/README.md
```

Há duas formas de rodar este sistema: **manual**, colando `project-instructions.md`
e `knowledge/` num Projeto do Claude Pro (seção abaixo); ou **automatizada**,
rodando `automation/orchestrator.py`, que chama a API da Claude diretamente e
executa o pipeline completo (CEO + agentes) sem intervenção manual — ver
`automation/README.md`.

## Como configurar no Claude Pro

1. Abra **claude.ai** → **Projects** → **Create project**.
2. Nomeie o projeto (ex.: "AI Music & Video Architect" ou "Creative Studio Engine").
3. Em **Project Instructions**, cole o conteúdo de `project-instructions.md`.
4. Em **Project Knowledge**, suba os 4 arquivos da pasta `knowledge/`.
5. Inicie uma conversa dentro do projeto com:

   ```
   Inicie o workflow para: [sua ideia aqui]
   ```

## Os 4 agentes internos (sub-personas)

| # | Agente | Função |
|---|--------|--------|
| 1 | **Analista de Conceito** | Decodifica a ideia bruta em tema emocional, mood e paleta de cores |
| 2 | **Luthier Digital (Suno Specialist)** | Gera o prompt de estilo e a letra estruturada para o Suno |
| 3 | **Diretor de Fotografia (Video Specialist)** | Gera prompts de cena para Runway/Luma com movimento, luz e lente |
| 4 | **Agente de Loop (Crítico)** | Verifica harmonia tonal/rítmica entre áudio e vídeo e força um refino se necessário |

## O loop na prática

**Input:** "Quero um clipe de um samurai futurista em Neo-Tóquio, música eletrônica pesada."

1. **Conceito:** Cyberpunk, melancolia, ação rápida.
2. **Suno:** `[Dark Cyberpunk, Industrial Techno, Heavy Distortion, 130 BPM, Male Vocals, Aggressive]`
3. **Vídeo:** `Cinematic wide shot, samurai with neon katana walking through rain, Tokyo city lights, low angle, slow motion, 35mm lens, hyper-realistic --ar 16:9`
4. **Crítico:** detecta que 130 BPM (rápido) não combina com "slow motion" — refina o
   vídeo para cortes rápidos (fast-paced cuts) *ou* a música para um synth ambiente
   mais lento, e reemite a versão final.

Esse ciclo de gerar → criticar → refinar é o que diferencia este sistema de um simples
gerador de prompt único.
