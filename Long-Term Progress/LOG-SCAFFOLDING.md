# Log Scaffolding: keeping years of daily progress readable

At one entry a day, seven days a week, for two to three years, the daily record will run to well over a thousand entries. **The author set up its structure on 2026-11-26: one log file per month, in a folder per year.** This guide sets out how sessions use it so that:

- `README.md` stays short enough to read at the start of every session;
- nothing is ever lost or rewritten;
- several sessions working at once never collide.

*(Rewritten 2026-11-26 for the author's monthly layout; it replaces the earlier plan of one `log/YYYY.md` file per year.)*

## The structure

```
Long-Term Progress/
├── README.md                          ← status table, rules, and the short log of changes to the tracker itself
├── LOG-SCAFFOLDING.md                 ← this guide
└── logs/
    ├── template_(clean).md            ← the blank entry, to copy from
    ├── template_(explanatory).md      ← the same, with the author's notes on what each part means
    ├── Overprocess_summary_catalog.md ← what each Overprocess is (ULM, DCI, MISE, CST, RWBEM)
    ├── Incremental_Progress_summary_catalog.md ← what each Long-Term Progress topic is (its counterpart)
    ├── 2026/2026-11.md, 2026-12.md
    ├── 2027/2027-01.md … 2027-12.md
    └── 2028/2028-01.md … 2028-12.md
```

- **One file per month,** named `logs/YYYY/YYYY-MM.md`, in a folder for its year.
- **The author made the month files through December 2028.** Most of them start as empty files. If a month's file is missing (a month before or after that range) or empty, create or fill it from `template_(clean).md`: the title `# Progress Log: <Month> <Year>`, the Monthly Summary, and the `## Daily Progress` heading.
- **The status table never moves.** It stays in `README.md`, because it shows where things stand *now*.

## What a day's entry holds

Each day gets one heading, `### <Month> <Day>, <Year>` (for example `### November 26, 2026`), with the three parts of the template:

1. **Overprocess:** which of the big build's Overprocesses moved that day (ULM, DCI, MISE, CST, RWBEM; see the catalog), each as its own bullet with its activity nested under it.
2. **Long-Term Progress:** each topic from the author's list worked on that day (more than one is fine), each as its own bullet, with its short daily summary nested under it and the mini-achievements under the summary. Nesting keeps clear which summary belongs to which topic. (Entries before November 26, 2026 use the earlier flat layout and stay as written; the November 26 entry was re-indented to the nested layout at the author's word, with no wording changed.)
3. **Resource Usage:** tokens, in millions, and the weekly allotment, in percent. **Tokens** come from the ledgers where there are any (for the DCI springboard runs, the Cost ledger in the Culture Library's `Springboarding/_dispatch/SPRINGBOARD_PROGRESS.md`); write "not measured" where there's no ledger. **The allotment** is the author's own meter reading for that day, with its time; never an estimate passed off as a reading (an estimate is labeled as one).

`template_(explanatory).md` has the author's own notes on each part.

## How sessions write it

1. **Re-read the month's file right before you edit it.** Several sessions may be writing the same day.
2. **Find today's heading, or add it at the bottom** of `## Daily Progress`, in date order.
3. **Add to the day; never rewrite it.** If today's entry already exists, add your Overprocess activity or your topic and its mini-achievements under the right part, below what is there. Don't reword, merge or reorder another session's lines.
4. **One day, one heading.** Never make a second heading for the same date.
5. **Resource Usage:** if another session has already recorded a figure for the day, don't overwrite it. Add yours as a separate line naming your session, or leave the day's total for the author.
6. **The Monthly Summary** is written at the month's end, or when the author asks; it summarizes, and changes no daily entry.
7. **Also update `README.md`:** the topic's row in the status table (last step with its date, next small piece), as the README's rules say.

## Rules

- **Never delete an entry.** A closed month's file is an archive: it is never edited again, except to fix a factual error the author points out.
- **Never rewrite history.** If an old entry is wrong, the author decides the fix, and the correction goes into today's entry, naming the date of the wrong one.
- **Stages stay the author's,** as everywhere else.
- **Keep this guide in step with the templates.** If the author changes the template, follow the template.
- **The folder is in the Archive Vault repo.** Ask the author before committing or pushing, as the Archive Vault rules require.
