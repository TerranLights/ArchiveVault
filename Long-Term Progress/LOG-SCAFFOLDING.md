# Log Scaffolding: keeping years of daily progress readable

At one or more lines a day, seven days a week, for two to three years, the progress log in `README.md` will grow to well over a thousand lines. This guide sets out how to split it so that:

- `README.md` stays short enough to read at the start of every session;
- nothing is ever lost or rewritten;
- several sessions working at once never collide.

**This structure is not set up yet.** Build it the first time the trigger below is met, following these steps exactly.

## The target structure

```
Long-Term Progress/
├── README.md             ← status table + the current year's log only
├── LOG-SCAFFOLDING.md    ← this guide
└── log/
    ├── README.md         ← index of the year files
    ├── 2026.md
    ├── 2027.md
    └── 2028.md
```

- **One file per calendar year,** named by the year: `log/YYYY.md`.
- **Year files are archives.** Once a year is closed, its file is never edited again, except to fix a factual error the author points out.
- **The status table never moves.** It always stays in `README.md`, because it shows where things stand *now*.

## When to split

**Trigger:** the first session that works on or after **January 1** of a new year, and finds lines from the previous year still in `README.md`'s log.

That session closes the previous year before it adds its own log line. This applies only at the year boundary. Never split mid-year, even if the log feels long. One fixed rule means parallel sessions never have to guess whether someone else is about to split.

## How to split (step by step)

1. **Re-read `README.md` right now,** immediately before you edit, as the README's rule 5 requires for parallel sessions.
2. **If `log/` doesn't exist yet, create it,** along with `log/README.md` (template below).
3. **Create `log/YYYY.md`** for the year being closed (template below).
4. **Move, don't copy.** Cut every log line dated in that year out of `README.md` and paste it into `log/YYYY.md`, unchanged and in the same order. Don't reword, merge, summarize or reorder anything.
5. **Check the count.** The number of lines in `log/YYYY.md` must equal the number removed from `README.md`. If they differ, stop and fix it before going on.
6. **Add the year to `log/README.md`'s index,** with its line count and the stage of each item at year's end, taken from the status table as it stands.
7. **Add a line to `README.md`'s log** recording the split, then your own line for the day's piece:
   `- YYYY-MM-DD (session) Log: closed YYYY into log/YYYY.md (N lines).`
8. **If the folder is under git** (the Archive Vault repo), commit the split on its own, separate from any other change, so the move shows up cleanly in history. Ask the author before committing or pushing, as the Archive Vault rules require.

## Templates

### `log/README.md`

```markdown
# Progress log archive

Closed years of the Long-Term Progress log, one file per year. The current year's log is in `../README.md`. These files are never edited after closing.

| Year | File | Lines | Stages at year's end |
|---|---|---|---|
| 2026 | [2026.md](2026.md) | N | Character arcs 0, Tepenian language 0, ... |
```

### `log/YYYY.md`

```markdown
# Progress log: YYYY

Closed on YYYY-MM-DD by (session). Moved unchanged from `../README.md`. Do not edit.

- YYYY-MM-DD (session) Item: what was done. Next: the next small piece.
- ...
```

## Rules

- **Never delete a log line.** Lines move from `README.md` to a year file; they don't disappear.
- **Never rewrite history.** If an old line is wrong, the author decides the fix, and the correction goes in as a new line in the current log that names the date of the wrong one.
- **Stages stay the author's,** as everywhere else. The "stages at year's end" column copies the table and decides nothing.
- **Keep this guide in step with the README.** If the log format in `README.md` changes, update the templates here to match.
