# Engram schema

Ship a self-contained directory. Research filenames are fixed so the
six-agent pass is interchangeable.

```
<skills-root>/engrams/<slug>/
  SKILL.md                 # filled from skill-template.md
  CONSTITUTION.md          # copy of distiller invariants
  MIND.md                  # compact models + heuristics
  PERSON.md
  STAKES.md               # Stage 8: why / skin / productive urgency                # relational texture
  MEMORY.md                # admitted traces
  RELATIONSHIPS.md         # per documented other; may be empty
  FIDELITY.md              # from fidelity-scorecard.md
  references/research/
    01-writings.md
    02-conversations.md
    03-expression-dna.md
    04-external-views.md
    05-decisions.md
    06-timeline.md
    07-intimate.md         # only if user supplied intimate corpus
  sources/
    books/
    transcripts/
    articles/
```

No `sources/media/`. Raw audio/video is transcribed into `transcripts/`.
Ledger 07 exists only after consented texture files; memos stay in 05.

`<slug>` is lowercase hyphenated (`ada-lovelace`). Not `-perspective`.

## MEMORY.md trace record

```
### TRACE-<id>
- type: episodic | semantic-self | procedural | relational | affective
- when: <date or range, or unknown>
- who: <people present>
- where: <place or unknown>
- cue: <retrieval cue>
- content: <stored content; subject's register if sourced>
- source: <primary locator>
- tests: specific · reactivated · sufficient · necessary
- valence: <sourced, or unrecorded>
- status: admitted | silent | rejected
```

Silent traces are known holes. Never narrate them as remembered.
Rejected traces stay in a short reject log so invention cannot return.
