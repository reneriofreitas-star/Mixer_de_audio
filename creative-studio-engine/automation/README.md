# Automação — Creative Studio Engine

Sistema real de automação (não role-play dentro de um chat): um script Python que
chama a API da Claude diretamente, orquestra os agentes especialistas em pipeline,
roda um loop de crítica/revisão, e só grava o entregável final quando o **CEO**
aprova.

## Organograma e autoridade de decisão

```
                         ┌────────────────────┐
                         │        CEO          │   aprova / reprova o pacote final
                         │  (claude-opus-5,     │   autoridade máxima — pode travar
                         │   effort: max)       │   a entrega mesmo com gates "ok"
                         └──────────┬───────────┘
                                    │ julga o pacote completo + histórico
                                    │
        ┌───────────────────────────┴───────────────────────────┐
        │                    PIPELINE DE CRIAÇÃO                  │
        │                                                          │
   ┌────▼─────┐    ┌──────────────┐    ┌───────────┐    ┌─────────▼────────┐
   │ Analista │───▶│   Luthier    │───▶│ Engenheiro │   │  Diretor de       │
   │ de       │    │   Digital    │    │ de Som     │   │  Fotografia       │
   │ Conceito │    │   (Suno)     │    │ (opcional) │   │  (Vídeo)          │
   └──────────┘    └──────┬───────┘    └─────┬──────┘    └─────────┬────────┘
                           │                  │                     │
                    ┌──────▼──────┐           │                     │
                    │  Letrista   │           │                     │
                    │  Ritual     │           │                     │
                    │ (opcional)  │           │                     │
                    └─────────────┘           │                     │
                                                │                     │
        ┌───────────────────────────────────────┴─────────────────────┘
        │                     GATES DE VALIDAÇÃO (loop)
        │
   ┌────▼──────────────┐         ┌──────────────────────┐
   │ Guardião da        │         │ Agente de Loop        │
   │ Identidade Visual  │         │ (Crítico)              │
   │ — só em projetos   │         │ — coerência BPM×câmera │
   │ com bíblia visual  │         │   e mood×lighting       │
   └────────────────────┘         └──────────────────────┘
        │  reprovou → devolve para Diretor de Fotografia com feedback
        │  (ciclo se repete até passar ou até max_loops)
```

**Regra de decisão**: nenhum agente especialista tem poder de aprovar a própria
saída. Os dois gates (Guardião Visual, Crítico) só podem reprovar e devolver para
revisão — quem aprova a entrega final é sempre o CEO, depois de ver o pacote
completo e o histórico de quantas rodadas de revisão foram necessárias. Se o
pipeline girar `max_loops` vezes sem convergir, o CEO recebe isso como sinal de
problema estrutural (não aprova só para "encerrar o loop").

## Os 8 agentes

| Agente | Arquivo de prompt | Quando roda | Pode reprovar? |
|---|---|---|---|
| **CEO** | `agents/ceo.md` | sempre, por último | decide aprovar/reprovar o pacote inteiro |
| Analista de Conceito | `agents/analista_conceito.md` | sempre, primeiro | não |
| Luthier Digital (Suno) | `agents/luthier_digital.md` | sempre | não |
| Engenheiro de Som | `agents/engenheiro_som.md` | só com `--sound-design` | não |
| Letrista Ritual | `agents/letrista_ritual.md` | só com `--lyrics` | não |
| Diretor de Fotografia | `agents/diretor_fotografia.md` | sempre | não |
| Guardião da Identidade Visual | `agents/guardiao_visual.md` | só se `--project emrys` (ou outro projeto com bíblia visual) | **sim** |
| Agente de Loop (Crítico) | `agents/agente_loop_critico.md` | sempre | **sim** |

Adicionar um agente novo = criar um novo arquivo em `agents/` + registrar em
`AGENT_REGISTRY` no `orchestrator.py`. O pipeline não tem um número fixo de agentes.

## Como rodar

```bash
cd creative-studio-engine/automation
pip install -r requirements.txt

# autenticação — qualquer uma das duas opções:
ant auth login                       # recomendado
# ou: export ANTHROPIC_API_KEY=sk-ant-...

python orchestrator.py --idea "samurai futurista em Neo-Tóquio, música eletrônica pesada" \
                        --project emrys \
                        --sound-design \
                        --lyrics
```

Flags:
- `--idea` (obrigatório): a ideia bruta.
- `--project`: `emrys` (usa a mitologia/identidade visual/gates do projeto EMRYS) ou
  `generic` (usa só o engine genérico, sem Guardião Visual). Default: `generic`.
- `--sound-design`: ativa o Engenheiro de Som Psicoacústico.
- `--lyrics`: ativa o Letrista Ritual.
- `--max-loops`: máximo de rodadas de revisão antes de escalar ao CEO mesmo sem
  convergência total. Default: `3`.

O resultado final (pacote aprovado ou reprovado, com o parecer do CEO e o histórico
completo do loop) é gravado em `output/<timestamp>_<slug>.md`.

## Custo e modelo

Todos os agentes usam `claude-opus-5` (nenhum downgrade automático para modelo mais
barato — essa é uma decisão do usuário, não do orquestrador). O sistema usa prompt
caching (`cache_control: ephemeral`) nos blocos de conhecimento anexados a cada
agente, já que o mesmo conteúdo (dicionários, constituição) se repete em várias
chamadas dentro de uma mesma execução e entre rodadas do loop de revisão.
