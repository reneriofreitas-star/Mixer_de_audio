# Dicionário de Movimentos de Câmera

Referência de conhecimento para o agente "Diretor de Fotografia". Suba este arquivo
em Project Knowledge no Claude.

## Movimentos básicos (câmera fixa em um eixo)

- **Pan (panorâmica horizontal)** — a câmera gira no eixo vertical, esquerda↔direita,
  sem se deslocar. Uso: revelar espaço, acompanhar movimento lateral.
- **Tilt (panorâmica vertical)** — a câmera gira no eixo horizontal, cima↔baixo.
  Uso: revelar altura, seguir um personagem se levantando.
- **Whip Pan** — pan extremamente rápido, gera desfoque de movimento (motion blur).
  Uso: transição de cena, choque, energia.
- **Static / Locked-off Shot** — câmera completamente parada, sem movimento.
  Uso: tensão contida, composição formal, observação distante.

## Movimentos de deslocamento (a câmera se move fisicamente)

- **Dolly In / Dolly Out** — câmera se move para frente/para trás em linha reta,
  geralmente sobre trilhos. Uso: aproximação/afastamento suave, foco emocional.
- **Truck Left / Truck Right (ou "Tracking Shot" lateral)** — câmera se desloca
  lateralmente, paralela à ação. Uso: acompanhar um personagem andando.
- **Pedestal Up / Pedestal Down** — câmera sobe ou desce verticalmente mantendo o
  ângulo. Uso: mudar a perspectiva de poder/vulnerabilidade.
- **Crane Shot / Jib Shot** — câmera montada em um braço mecânico, permite
  movimentos verticais e horizontais amplos e suaves. Uso: revelações épicas,
  planos de abertura.
- **Steadicam** — câmera estabilizada carregada por operador, movimento fluido
  mesmo andando. Uso: seguir personagem por ambientes complexos sem cortes.
- **Handheld** — câmera na mão, movimento levemente instável. Uso: urgência,
  realismo documental, tensão.
- **Drone / Aerial Shot** — vista aérea, pode ser estática ou em movimento
  (ex.: "slow aerial push-in"). Uso: estabelecer escala, paisagens.

## Movimentos combinados / avançados

- **Tracking Shot** — termo genérico para câmera que acompanha um sujeito em
  movimento (pode combinar truck + pan).
- **Orbit Shot / Arc Shot** — câmera circula ao redor do sujeito, mantendo-o no
  centro do quadro. Uso: destacar um objeto/personagem, momentos de revelação.
- **Dolly Zoom (efeito Vertigo)** — dolly in enquanto a lente faz zoom out (ou
  vice-versa), mantendo o sujeito do mesmo tamanho mas distorcendo o fundo. Uso:
  desorientação, choque psicológico.
- **Push-In** — variação do dolly in mais lenta e sutil, comum para aumentar tensão
  emocional gradualmente.
- **Crash Zoom** — zoom rápido e abrupto. Uso: ênfase cômica ou de choque.
- **Snorricam** — câmera presa ao corpo do ator, o fundo se move mas o rosto fica
  fixo no quadro. Uso: intensidade psicológica, embriaguez, pânico.

## Enquadramento (ângulo, não movimento, mas combinável)

- **Low Angle** — câmera abaixo do sujeito, olhando para cima. Transmite poder.
- **High Angle** — câmera acima do sujeito, olhando para baixo. Transmite
  vulnerabilidade.
- **Dutch Angle / Canted Angle** — câmera inclinada no eixo. Transmite instabilidade.
- **Eye Level** — altura neutra dos olhos. Transmite naturalidade/neutralidade.
- **Bird's Eye View** — vista direta de cima. Uso: geometria, escala, isolamento.
- **Worm's Eye View** — vista direta de baixo. Uso: grandiosidade, opressão.

## Combinações prontas para prompts (exemplos)

- `slow dolly-in, low angle, static frame`
- `handheld tracking shot, following subject through crowd`
- `sweeping crane shot, revealing cityscape, high angle transitioning to eye level`
- `orbit shot around subject, shallow depth of field`
- `whip pan transition into fast-paced handheld action`
