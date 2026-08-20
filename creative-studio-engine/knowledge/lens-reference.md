# Referência de Lentes e Distância Focal

Referência de conhecimento para o agente "Diretor de Fotografia". Suba este arquivo
em Project Knowledge no Claude.

## Distância focal (efeito na imagem)

| Lente | Categoria | Campo de visão | Efeito visual | Uso típico em prompt |
|---|---|---|---|---|
| 8mm | Fisheye | Extremamente amplo (~180°) | Distorção curva forte nas bordas | `8mm fisheye lens, distorted wide view` |
| 14–24mm | Ultra-wide | Muito amplo | Exagera profundidade, distorce bordas levemente | `16mm ultra-wide lens, expansive landscape` |
| 35mm | Wide-normal | Amplo, natural | Pouca distorção, sensação imersiva, comum em cinema | `35mm lens, cinematic naturalism` |
| 50mm | Normal | Similar à visão humana | Neutro, sem distorção perceptível | `50mm lens, natural perspective` |
| 85mm | Curta telefoto | Moderadamente estreito | Comprime levemente, ótimo para retratos, isola sujeito | `85mm lens, shallow depth of field, portrait compression` |
| 135mm+ | Telefoto | Estreito | Comprime fortemente o fundo, "achata" a perspectiva | `135mm telephoto, compressed background, subject isolation` |
| 200mm+ | Super telefoto | Muito estreito | Compressão extrema, uso esportivo/vida selvagem | `300mm super telephoto, distant subject compression` |

## Tipos especiais de lente

- **Anamorphic Lens** — proporção widescreen nativa (2.39:1), bokeh oval
  horizontal, flares azuis/horizontais característicos. Uso: estética de blockbuster
  hollywoodiano. `anamorphic lens, horizontal lens flare, oval bokeh`
- **Macro Lens** — foco extremamente próximo, revela textura/detalhe minúsculo.
  `macro lens, extreme close-up detail`
- **Tilt-Shift Lens** — permite inclinar o plano de foco, cria efeito "miniatura".
  `tilt-shift lens, miniature effect`
- **Vintage/Lomo Lens** — aberrações ópticas propositais, baixo contraste, cores
  quentes. `vintage lomo lens, soft glow, warm color cast`

## Abertura e profundidade de campo (bokeh)

- **f/1.4 – f/2.8 (abertura ampla)** — profundidade de campo rasa, fundo fortemente
  desfocado (bokeh cremoso). `shallow depth of field, creamy bokeh`
- **f/4 – f/8 (abertura média)** — equilíbrio entre sujeito nítido e algum contexto
  de fundo. `medium depth of field`
- **f/11+ (abertura fechada)** — tudo em foco, comum em paisagens.
  `deep depth of field, everything in focus`

## Movimento de foco

- **Rack Focus** — a lente transfere o foco de um sujeito para outro durante a
  tomada. `rack focus from foreground to background`
- **Focus Pull** — ajuste manual e suave de foco durante o movimento de câmera.

## Combinações prontas para prompts (exemplos)

- `85mm lens, shallow depth of field, warm bokeh, portrait compression`
- `35mm anamorphic lens, horizontal flare, wide cinematic frame --ar 2.39:1`
- `8mm fisheye, distorted perspective, chaotic energy`
- `135mm telephoto, compressed cityscape background, subject isolation`
- `tilt-shift lens, miniature effect, aerial cityscape`
