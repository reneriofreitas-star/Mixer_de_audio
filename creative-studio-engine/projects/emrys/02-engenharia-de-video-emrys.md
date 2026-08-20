# Engenharia de Vídeo — Projeto EMRYS

> Aplica o framework `[Subject] [Action] [Camera Movement] [Lighting] [Style]` do
> `project-instructions.md` geral, usando o vocabulário de
> `knowledge/camera-dictionary.md`, `knowledge/lens-reference.md` e
> `knowledge/lighting-glossary.md`, cruzado com a identidade visual de
> `01-identidade-visual-emrys.md` e o protocolo de 4 fases da constituição
> (`00-constituicao-emrys.md`, Seção 6).

## 0. Prompt-âncora de personagem (usar sempre como base, para consistência entre cenas)

```
EMRYS: an ageless, androgynous archmage figure, cracked ash-and-ember skin that
glows faintly from within, wearing a flowing multi-empire cloak stitched from
bronze Babylonian circuitry patterns, Egyptian gold linework, Persian fire-silk,
and Celtic knotwork, a crown of luminous sacred geometry hovering above the head,
golden seed-particles drifting off the cloak with every movement, bare feet
grounded in red terreiro dust, a wooden berimbau in hand, capoeira-informed ginga
stance, hyper-detailed, cinematic
```

Reutilize este bloco como base fixa em todas as cenas abaixo, ajustando apenas os
campos de ação/câmera/luz por fase.

## 1. Fase 1 — O Esquecido (0–2min · silêncio, Ney solo, chocalhos dispersos)

**Coerência de loop**: sem batida definida ainda — câmera deve ser quase imóvel,
reforçando o "cansaço do córtex pré-frontal" antes do despertar.

**Cena 1.1**
```
[Subject] EMRYS (ver prompt-âncora), capuz cobrindo o rosto, cinzas frias sem brilho
[Action] completamente imóvel, apenas o manto se move levemente com o vento
[Camera Movement] static / locked-off shot, extreme long shot
[Lighting] low-key lighting, near-silhouette, single distant hard light source
[Style] 35mm lens, deep shadow, muted desaturated palette, film grain --ar 16:9
```

**Cena 1.2**
```
[Subject] close-up nas mãos de EMRYS segurando chocalhos de sementes
[Action] sementes caem lentamente de dentro da mão fechada, dispersando no ar
[Camera Movement] extremely slow push-in, rack focus from foreground dust to hand
[Lighting] soft diffused light, cool moonlight tone
[Style] 85mm lens, shallow depth of field, macro-like intimacy --ar 16:9
```

## 2. Fase 2 — O Despertar da Memória (2–5min · Tambor Xamânico 55 BPM + Bodhrán, busca do 528Hz)

**Coerência de loop**: BPM baixo/moderado (55 half-time) → movimento de câmera lento
mas já com deslocamento físico (primeiros passos), nunca cortes rápidos.

**Cena 2.1**
```
[Subject] EMRYS (prompt-âncora), brasas sob a pele começam a pulsar
[Action] primeiro passo dado, pé descalço toca a poeira vermelha do terreiro
[Camera Movement] slow dolly-in, low angle
[Lighting] transitioning low-key to warm amber glow, practical ember light rising
[Style] 35mm lens, warm color grade emerging from cold, subtle lens flare --ar 16:9
```

**Cena 2.2**
```
[Subject] EMRYS, coroa geométrica começando a se formar por partículas convergindo
[Action] cabeça se ergue lentamente, olhar ainda oculto
[Camera Movement] slow pedestal up combined with gentle orbit
[Lighting] rim light beginning to define silhouette edge, amber and gold tones
[Style] 50mm lens, medium depth of field, particles catching light --ar 16:9
```

## 3. Fase 3 — O Retorno do Verbo (5–7min · Carnyx + Cláirseach + Santur, base Berimbau/Maracatu no centro)

**Coerência de loop**: BPM sobe para 122 (pico rítmico) → aqui a câmera pode e deve
ser a mais dinâmica de todo o vídeo — crane, orbit, tracking.

**Cena 3.1**
```
[Subject] EMRYS, manto totalmente aberto, coroa geométrica completa e luminosa, berimbau em punho
[Action] ginga ativa, corpo em movimento pleno, partículas douradas se espalhando com força
[Camera Movement] sweeping crane shot revealing full figure, transitioning into orbit shot around subject
[Lighting] high-contrast, strong golden rim light, backlit particles
[Style] 35mm anamorphic lens, horizontal lens flare, epic scale --ar 2.39:1
```

**Cena 3.2**
```
[Subject] EMRYS tocando o berimbau em primeiro plano, terreiro ao fundo
[Action] toque rítmico do berimbau sincronizado ao pulso de 122 BPM, fagulhas de brasa saltando
[Camera Movement] fast-paced handheld tracking shot, circling the performer
[Lighting] volumetric god rays through dust, warm hard key light
[Style] 50mm lens, deep depth of field, dust and ember particles in frame --ar 16:9
```

**Cena 3.3**
```
[Subject] as 3 vozes femininas (espíritos de Hathor) surgindo como figuras etéreas ao redor de EMRYS
[Action] elas respondem ao chamado do berimbau, formando um coro visual ao redor da figura central
[Camera Movement] orbit shot, wide to medium
[Lighting] ethereal soft backlight, catedral-like volumetric haze, cool-to-warm gradient
[Style] 35mm lens, dreamlike bloom, painterly cinematic grade --ar 16:9
```

## 4. Fase 4 — A Sugestão Pós-Hipnótica (7–8min · tudo cessa exceto o pulso do Berimbau, Spoken Word)

**Coerência de loop**: energia despenca para quase-silêncio — a câmera deve
desacelerar drasticamente e convergir para um único ponto (o rosto), espelhando a
coroa geométrica reduzindo a um ponto de luz.

**Cena 4.1**
```
[Subject] EMRYS, coroa geométrica reduzindo-se a um único ponto de luz
[Action] corpo se aquieta por completo, apenas a mão pulsa levemente no berimbau
[Camera Movement] slow push-in ending in static hold, extreme close-up on face
[Lighting] progressive darkening, only rim light and single point-light remain
[Style] 85mm lens, shallow depth of field, high contrast fading to black --ar 16:9
```

**Cena 4.2 (encerramento)**
```
[Subject] silhueta de EMRYS
[Action] nenhum movimento; corte para preto absoluto
[Camera Movement] static / locked-off shot
[Lighting] silhouette against near-total darkness, single fading ember point
[Style] 35mm lens, minimal grain, fade to black over 12 seconds (espelha os 12s de reverb do áudio) --ar 16:9
```

## 5. Nota do Agente de Loop (crítico) para este projeto

Ao gerar qualquer cena para EMRYS, o Agente de Loop deve validar, além da checagem
padrão BPM×movimento:

1. O prompt contém pelo menos 2 dos 3 traços centrais da identidade (cinza/brasa,
   manto multi-império, coroa geométrica)? Se não, revisar.
2. Há referência afro-brasileira explícita (berimbau, terra do terreiro, ou ginga)
   em pelo menos um plano da fase? Se não, é falha de Regra de Ouro — obrigatório
   corrigir antes de entregar.
3. A intensidade de movimento de câmera acompanha a curva de energia da fase
   (Fase 1 quase estática → Fase 3 pico dinâmico → Fase 4 desaceleração até o
   estático final)?

Se qualquer um desses 3 pontos falhar, o resultado não pode ser entregue como final
— é sempre a Regra de Ouro Visual (Seção 3 de `01-identidade-visual-emrys.md`) que
tem prioridade máxima sobre qualquer outro ajuste estético.
