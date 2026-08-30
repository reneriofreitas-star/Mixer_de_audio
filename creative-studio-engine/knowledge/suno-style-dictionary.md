# Dicionário de Estilos e Tags do Suno AI

Referência de conhecimento para o agente "Luthier Digital". Suba este arquivo em
Project Knowledge no Claude.

## 1. Como o Suno interpreta prompts

O campo "Style of Music" aceita uma lista de tags/descritores separados por vírgula,
geralmente entre colchetes quando combinados a instruções de estrutura dentro da
letra. Quanto mais específica e tecnicamente coerente a combinação, melhor o
resultado. Ordem recomendada:

```
[Gênero principal, Sub-gênero/influência, Instrumentação-chave, Tags de produção,
Tipo de vocal, BPM aproximado, Mood]
```

## 2. Gêneros e sub-gêneros mais reconhecidos

**Eletrônica:** Synthwave, Darksynth, Dark Techno, Industrial Techno, Drum and Bass,
Dubstep, Trance, Progressive House, Deep House, Ambient Electronic, IDM, Chillwave,
Vaporwave, Future Bass, Trap (EDM).

**Rock/Metal:** Alternative Rock, Post-Rock, Indie Rock, Grunge, Punk Rock,
Hard Rock, Heavy Metal, Symphonic Metal, Metalcore, Progressive Metal, Shoegaze.

**Hip-Hop/Urbano:** Boom Bap, Trap, Lo-fi Hip-Hop, Drill, Cloud Rap, Conscious
Hip-Hop, R&B, Neo-Soul.

**Orquestral/Cinematográfico:** Orchestral Hybrid, Epic Trailer Score, Cinematic
Ambient, Neoclassical, Film Score, Choral, Minimalist Piano.

**Popular Brasileiro:** MPB, Bossa Nova, Samba, Sertanejo, Forró, Pagode, Axé,
Brega Funk, Funk Carioca.

**Folk/Acústico:** Indie Folk, Acoustic Singer-Songwriter, Americana, Bluegrass,
Country.

**World/Étnico:** Afrobeat, Latin Fusion, Celtic, Middle Eastern Fusion, Flamenco.

**Jazz/Blues:** Smooth Jazz, Nu Jazz, Jazz Fusion, Blues Rock, Delta Blues.

## 3. Tags de produção (qualidade/mixagem)

`High Fidelity` · `Studio Recording` · `48kHz` · `Analog Warmth` · `Vinyl Crackle` ·
`Lo-fi Tape` · `Wide Stereo Mix` · `Punchy Mix` · `Layered Production` ·
`Live Recording` · `Radio Ready` · `Minimalist Mix`.

## 4. Tags de instrumentação

`Analog Synth Bass` · `808 Sub Bass` · `Heavy Distortion` · `Clean Electric Guitar` ·
`Fingerpicked Acoustic Guitar` · `Arpeggiated Synth` · `String Section` ·
`Brass Section` · `Solo Piano` · `Driving Drum Machine` · `Live Drum Kit` ·
`Hand Percussion` · `Choir Pads`.

## 5. Tags de vocal

`Male Vocals` · `Female Vocals` · `Duet` · `Falsetto` · `Ethereal Vocals` ·
`Aggressive Vocals` · `Whispered Vocals` · `Belting` · `Autotuned` · `Raspy Vocals` ·
`Layered Harmonies` · `Spoken Word` · `Instrumental` (ausência de vocal).

## 6. Tags de mood/energia

`Melancholic` · `Euphoric` · `Aggressive` · `Dreamy` · `Nostalgic` · `Triumphant` ·
`Tense` · `Playful` · `Romantic` · `Dark` · `Uplifting` · `Contemplative`.

## 7. Faixas de BPM de referência

| Faixa BPM | Sensação | Gêneros típicos |
|---|---|---|
| 60–80 | Lento, contemplativo | Ambient, Ballad, Downtempo |
| 80–100 | Groove moderado | R&B, Lo-fi Hip-Hop, Indie Folk |
| 100–120 | Andamento pop padrão | Pop, Rock, House |
| 120–140 | Energético/dançante | Techno, Trance, Drum funk |
| 140–160 | Alta energia | Drum and Bass, Hardstyle |
| 160+ | Extremo | Speedcore, Breakcore |

## 8. Tags de estrutura de letra (Suno reconhece dentro do campo de letra)

`[Intro]` `[Verse]` `[Verse 2]` `[Pre-Chorus]` `[Chorus]` `[Post-Chorus]`
`[Bridge]` `[Drop]` `[Build-up]` `[Break]` `[Hook]` `[Refrain]`
`[Instrumental Break]` `[Guitar Solo]` `[Outro]` `[Fade Out]`

## 9. Boas práticas

- Combine no máximo 4-6 tags de gênero/produção por prompt — excesso de tags dilui
  o resultado.
- Coloque o gênero principal sempre primeiro.
- Use BPM numérico apenas quando precisão rítmica for crítica (ex.: sincronizar com
  vídeo); caso contrário, descritores como "mid-tempo" funcionam bem.
- Tags conflitantes (ex.: "Aggressive" + "Dreamy" sem contexto) geram resultados
  imprevisíveis — se misturar moods, explique a intenção na letra/estrutura.
