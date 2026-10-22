# Japanese grammar-logic diagrams — provisional pair, archived 2026-10-21

**Origin project:** `slang-synthesis` (language-extraction repo)
**Why archived:** superseded in method, not in content — see below. Kept because they record a line
of reasoning worth being able to revisit.

## What these are

Two SVG diagrams of Japanese grammar logic, built in October 2026 as the first attempt to extend the
user's hand-made English grammar-logic notation system to another language:

- `01_kosoado_domain_assignment.svg` — the こそあど system as 領域の割り当て (domain assignment): one
  question, 「それは誰の領域か」, asked on three fields (場所 / 知識 / 心理)
- `02_wa_ga_direction_of_weight.svg` — は sends the sentence's weight forward, が sends it backward
- `00_original_index.md` — the index that shipped with them, including sourcing and a note on what
  changed between the first and second versions of diagram 01

## Why they were superseded

**Not because the analysis was wrong — because they were made in the wrong order.** The project
subsequently established a five-stage procedure in which diagrams are the *output* of a finished
analysis, never the instrument for doing one:

1. establish what the official grammars say
2. identify the mechanisms
3. study the mechanisms (adversarial testing)
4. identify what the deeper logic actually is
5. work out the logic behind the specific functionality

These two were drawn before stages 1–3 existed for Japanese. They were flagged provisional in place
for that reason, then archived once that status became permanent.

Diagram 01 has a second problem: its first version put an "English" panel beside a "日本語" panel,
making English the measuring stick and Japanese the deviation. It was rebuilt Japanese-internally
before archiving, but the rebuild is still pre-analysis.

## What held up, and what did not

**Held up.** Diagram 02's forward/backward account was independently corroborated twice after these
were drawn — by Jay Rubin (*Making Sense of Japanese: What the Textbooks Don't Tell You*), and by
Tanaka & Kubozono 『日本語の発音教室』 §4.4, which states it from the prosody side: 文法 → フォーカス →
イントネーション.

**Did not.** Diagram 02 treats は as uniformly forward-pointing. 『日本語の発音教室』 §4.4.1 shows
**contrastive は projects focus *backward*, patterning with が** — so は splits in two, and the diagram
does not show that.

## Where the live work is

In the origin repo, under `datasets/Japanese/grammar_logic/`:
- `.sweep/` — stage 1, all 420 established files
- `wa_ga.md` — stage 2, mechanism sorting
- `stage3/` — adversarial testing (prosody re-extraction; 617-hit negation study)
- `observations.md` — running analytical notes
- `native_speaker_queries/` — questions only a speaker can settle
