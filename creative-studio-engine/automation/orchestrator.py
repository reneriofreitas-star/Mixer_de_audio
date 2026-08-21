#!/usr/bin/env python3
"""Creative Studio Engine — orquestrador de agentes.

Pipeline real (chamadas de API, não role-play): Analista de Conceito -> Luthier
Digital (Suno) [-> Engenheiro de Som] [-> Letrista Ritual] -> Diretor de
Fotografia -> gates de validacao (Guardiao Visual, Agente de Loop/Critico) em loop
de revisao -> CEO decide aprovar ou reprovar o pacote final.

Uso:
    python orchestrator.py --idea "samurai futurista em Neo-Toquio, musica eletronica pesada" \
                            --project emrys --sound-design --lyrics
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path
from typing import List, Literal, Optional

import anthropic
from pydantic import BaseModel

MODEL = "claude-opus-5"
BASE_DIR = Path(__file__).resolve().parent
AGENTS_DIR = BASE_DIR / "agents"
ENGINE_DIR = BASE_DIR.parent
KNOWLEDGE_DIR = ENGINE_DIR / "knowledge"
EMRYS_DIR = ENGINE_DIR / "projects" / "emrys"
OUTPUT_DIR = BASE_DIR / "output"


# --------------------------------------------------------------------------- #
# Modelos de saida estruturada (gates de decisao)
# --------------------------------------------------------------------------- #

class GateResult(BaseModel):
    passed: bool
    issues: List[str] = []
    revision_target: Optional[Literal["audio", "video", "none"]] = "none"


class CEODecision(BaseModel):
    approved: bool
    summary: str
    notes: str


# --------------------------------------------------------------------------- #
# Utilitarios
# --------------------------------------------------------------------------- #

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_knowledge(paths: List[Path]) -> str:
    """Concatena arquivos de conhecimento em um unico bloco de referencia."""
    blocks = []
    for p in paths:
        if p.exists():
            blocks.append(f"### Referência: {p.name}\n\n{load_text(p)}")
    if not blocks:
        return ""
    return "\n\n---\n\n".join(blocks)


def build_system(agent_prompt_path: Path, knowledge_paths: List[Path]) -> str:
    agent_prompt = load_text(agent_prompt_path)
    knowledge = load_knowledge(knowledge_paths)
    if not knowledge:
        return agent_prompt
    return f"{agent_prompt}\n\n---\n\n# MATERIAL DE REFERÊNCIA ANEXADO\n\n{knowledge}"


def extract_bpm(text: str) -> Optional[str]:
    match = re.search(r"BPM:\s*([0-9]+(?:\s*x?\s*[0-9]*)?)", text)
    return match.group(1).strip() if match else None


class AgentError(RuntimeError):
    pass


def call_creative(client: anthropic.Anthropic, system: str, user_content: str,
                   effort: str = "high", max_tokens: int = 4096) -> str:
    """Chamada de texto livre (etapas criativas: conceito, suno, video, letra...)."""
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            thinking={"type": "adaptive"},
            output_config={"effort": effort},
            messages=[{"role": "user", "content": user_content}],
        )
    except anthropic.AuthenticationError:
        raise AgentError(
            "Falha de autenticação com a API da Claude. Rode `ant auth login` ou "
            "defina a variável de ambiente ANTHROPIC_API_KEY."
        )
    except anthropic.RateLimitError as e:
        retry_after = e.response.headers.get("retry-after", "60") if e.response else "60"
        raise AgentError(f"Rate limit atingido. Tente novamente em {retry_after}s.")
    except anthropic.APIStatusError as e:
        raise AgentError(f"Erro da API ({e.status_code}): {e.message}")
    except anthropic.APIConnectionError:
        raise AgentError("Erro de rede ao contatar a API da Claude.")

    if response.stop_reason == "refusal":
        category = response.stop_details.category if response.stop_details else None
        raise AgentError(f"Chamada recusada pela API (categoria: {category}).")

    text = "\n".join(b.text for b in response.content if b.type == "text")
    return text.strip()


def call_gate(client: anthropic.Anthropic, system: str, user_content: str) -> GateResult:
    """Chamada estruturada (gates de validação: Guardião Visual, Crítico)."""
    try:
        response = client.messages.parse(
            model=MODEL,
            max_tokens=2048,
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            output_config={"effort": "medium"},
            messages=[{"role": "user", "content": user_content}],
            output_format=GateResult,
        )
    except anthropic.AuthenticationError:
        raise AgentError(
            "Falha de autenticação com a API da Claude. Rode `ant auth login` ou "
            "defina a variável de ambiente ANTHROPIC_API_KEY."
        )
    except anthropic.APIStatusError as e:
        raise AgentError(f"Erro da API ({e.status_code}): {e.message}")
    return response.parsed_output


def call_ceo(client: anthropic.Anthropic, system: str, user_content: str) -> CEODecision:
    try:
        response = client.messages.parse(
            model=MODEL,
            max_tokens=2048,
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            output_config={"effort": "max"},
            messages=[{"role": "user", "content": user_content}],
            output_format=CEODecision,
        )
    except anthropic.AuthenticationError:
        raise AgentError(
            "Falha de autenticação com a API da Claude. Rode `ant auth login` ou "
            "defina a variável de ambiente ANTHROPIC_API_KEY."
        )
    except anthropic.APIStatusError as e:
        raise AgentError(f"Erro da API ({e.status_code}): {e.message}")
    return response.parsed_output


# --------------------------------------------------------------------------- #
# Pipeline
# --------------------------------------------------------------------------- #

def run(idea: str, project: str, sound_design: bool, lyrics: bool, max_loops: int) -> Path:
    client = anthropic.Anthropic()
    is_emrys = project == "emrys"

    def emrys_files(*names: str) -> List[Path]:
        return [EMRYS_DIR / n for n in names] if is_emrys else []

    log: List[str] = []

    def step(label: str) -> None:
        print(f"[{dt.datetime.now().strftime('%H:%M:%S')}] {label}")
        log.append(label)

    # 1. Analista de Conceito
    step("Analista de Conceito: mapeando ideia -> mood/paleta/energia")
    concept_system = build_system(
        AGENTS_DIR / "analista_conceito.md",
        emrys_files("00-constituicao-emrys.md"),
    )
    concept = call_creative(client, concept_system, f"Ideia bruta do usuário:\n{idea}")

    # 2. Luthier Digital
    step("Luthier Digital: gerando Style Prompt do Suno")
    luthier_system = build_system(
        AGENTS_DIR / "luthier_digital.md",
        [KNOWLEDGE_DIR / "suno-style-dictionary.md"] + emrys_files(
            "00-constituicao-emrys.md", "03-cavaquinho-hypnotic-lead.md"
        ),
    )
    suno_output = call_creative(client, luthier_system, f"Conceito:\n{concept}")

    # 2b. Engenheiro de Som (opcional)
    if sound_design:
        step("Engenheiro de Som: aprofundando textura psicoacústica")
        som_system = build_system(
            AGENTS_DIR / "engenheiro_som.md",
            [KNOWLEDGE_DIR / "suno-style-dictionary.md"] + emrys_files("03-cavaquinho-hypnotic-lead.md"),
        )
        suno_output = call_creative(
            client, som_system,
            f"Conceito:\n{concept}\n\nStyle Prompt atual:\n{suno_output}",
        )

    # 2c. Letrista Ritual (opcional)
    lyrics_output = None
    if lyrics:
        step("Letrista Ritual: escrevendo versos")
        letrista_system = build_system(
            AGENTS_DIR / "letrista_ritual.md",
            emrys_files("00-constituicao-emrys.md"),
        )
        lyrics_output = call_creative(
            client, letrista_system,
            f"Conceito:\n{concept}\n\nEstrutura/Style Prompt:\n{suno_output}",
        )

    # 3. Diretor de Fotografia
    step("Diretor de Fotografia: gerando prompts de vídeo")
    diretor_system = build_system(
        AGENTS_DIR / "diretor_fotografia.md",
        [KNOWLEDGE_DIR / "camera-dictionary.md", KNOWLEDGE_DIR / "lens-reference.md",
         KNOWLEDGE_DIR / "lighting-glossary.md"] + emrys_files(
            "01-identidade-visual-emrys.md", "02-engenharia-de-video-emrys.md"
        ),
    )

    def gen_video(feedback: Optional[str] = None) -> str:
        content = f"Conceito:\n{concept}\n\nStyle Prompt de áudio (para referência de BPM/energia):\n{suno_output}"
        if feedback:
            content += f"\n\nFEEDBACK DE REVISÃO:\n{feedback}"
        return call_creative(client, diretor_system, content)

    video_output = gen_video()

    # 4-5. Loop de gates (Guardião Visual + Crítico)
    guardiao_system = build_system(
        AGENTS_DIR / "guardiao_visual.md", emrys_files("01-identidade-visual-emrys.md")
    ) if is_emrys else None
    critico_system = build_system(
        AGENTS_DIR / "agente_loop_critico.md", emrys_files("00-constituicao-emrys.md")
    )

    def gen_audio_revision(feedback: str) -> str:
        return call_creative(
            client, luthier_system,
            f"Conceito:\n{concept}\n\nStyle Prompt atual:\n{suno_output}\n\nFEEDBACK DE REVISÃO:\n{feedback}",
        )

    iteration = 0
    converged = False
    while iteration < max_loops:
        step(f"Gates de validação — rodada {iteration + 1}")

        if guardiao_system:
            guardiao = call_gate(
                client, guardiao_system,
                f"Prompts de vídeo:\n{video_output}",
            )
        else:
            guardiao = GateResult(passed=True, issues=[])

        critico = call_gate(
            client, critico_system,
            f"Style Prompt de áudio:\n{suno_output}\n\nPrompts de vídeo:\n{video_output}",
        )

        log.append(
            f"  Guardião Visual: passed={guardiao.passed} issues={guardiao.issues}"
        )
        log.append(
            f"  Crítico: passed={critico.passed} issues={critico.issues} "
            f"revision_target={critico.revision_target}"
        )

        if guardiao.passed and critico.passed:
            converged = True
            break

        feedback_bits = list(guardiao.issues) + list(critico.issues)
        feedback = "\n".join(f"- {f}" for f in feedback_bits)

        needs_video_revision = (not guardiao.passed) or (
            not critico.passed and critico.revision_target == "video"
        )
        needs_audio_revision = (
            not critico.passed and critico.revision_target == "audio"
        )

        if needs_audio_revision:
            step("  Revisando áudio (Luthier Digital)")
            suno_output = gen_audio_revision(feedback)
        if needs_video_revision:
            step("  Revisando vídeo (Diretor de Fotografia)")
            video_output = gen_video(feedback)

        iteration += 1

    if not converged:
        step(f"AVISO: loop encerrado sem convergência após {max_loops} rodadas")

    # 6. CEO
    step("CEO: revisão final")
    ceo_system = load_text(AGENTS_DIR / "ceo.md")
    lyrics_block = f"Letra:\n{lyrics_output}\n" if lyrics_output else ""
    ceo_input = (
        f"Ideia original do usuário:\n{idea}\n\n"
        f"Conceito:\n{concept}\n\n"
        f"Style Prompt de áudio (final):\n{suno_output}\n\n"
        f"{lyrics_block}"
        f"Prompts de vídeo (final):\n{video_output}\n\n"
        f"Rodadas de revisão executadas: {iteration} de {max_loops} (convergiu: {converged})\n"
    )
    ceo_decision = call_ceo(client, ceo_system, ceo_input)

    # Gravação do resultado
    OUTPUT_DIR.mkdir(exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", idea.lower())[:40].strip("-")
    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = OUTPUT_DIR / f"{ts}_{slug}.md"

    status = "✅ APROVADO PELO CEO" if ceo_decision.approved else "❌ REPROVADO PELO CEO"
    lyrics_section = f"## Letra\n{lyrics_output}\n\n" if lyrics_output else ""
    log_text = "\n".join(log)
    doc = (
        f"# Creative Studio Engine — Entregável\n\n"
        f"**Ideia original**: {idea}\n"
        f"**Projeto**: {project}\n"
        f"**Status**: {status}\n\n"
        f"## Parecer do CEO\n{ceo_decision.summary}\n\n{ceo_decision.notes}\n\n"
        f"## Conceito\n{concept}\n\n"
        f"## Áudio (Suno)\n{suno_output}\n\n"
        f"{lyrics_section}"
        f"## Vídeo\n{video_output}\n\n"
        f"## Histórico do pipeline\n```\n{log_text}\n```\n"
    )
    out_path.write_text(doc, encoding="utf-8")
    step(f"Gravado em {out_path}")
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Creative Studio Engine — orquestrador de agentes")
    parser.add_argument("--idea", required=True, help="Ideia bruta do usuário")
    parser.add_argument("--project", choices=["generic", "emrys"], default="generic")
    parser.add_argument("--sound-design", action="store_true")
    parser.add_argument("--lyrics", action="store_true")
    parser.add_argument("--max-loops", type=int, default=3)
    args = parser.parse_args()

    try:
        out_path = run(args.idea, args.project, args.sound_design, args.lyrics, args.max_loops)
    except AgentError as e:
        print(f"\nErro: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"\nConcluído: {out_path}")


if __name__ == "__main__":
    main()
