#!/usr/bin/env python3
"""
Rebuild the master INDEX.md to reflect the new continent -> country -> zodiac
folder structure, and recreate the Aries/Taurus finding files that were lost
during the earlier restructure.
"""
import os

DCI = "/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Hermes_research/findings/DCI_(Deep_Culture_Investigation)"

# Targets: (number, name, continent)
TARGETS = [
    (1, "Cascadia", "North_America"),
    (2, "Alaska", "North_America"),
    (3, "Sonora", "North_America"),
    (4, "Korea", "East_Asia"),
    (5, "Sinian Federation", "East_Asia"),
    (6, "Japan", "East_Asia"),
    (7, "Australia", "Oceania"),
    (8, "CSA", "North_America"),
    (9, "United Kingdom", "Europe"),
    (10, "Indonesia", "Maritime_Southeast_Asia"),
    (11, "Germany", "Europe"),
    (12, "Brazil", "Latin_America"),
    (13, "France", "Europe"),
    (14, "Appalachia", "North_America"),
    (15, "New England", "North_America"),
    (16, "Austro-Bavaria", "Europe"),
    (17, "New Zealand", "Oceania"),
    (18, "Russia (core state)", "Russia"),
    (19, "Taiwan", "East_Asia"),
    (20, "Argentina (without Patagonia)", "Latin_America"),
    (21, "Vietnam", "Mainland_Southeast_Asia"),
    (22, "Malaysia", "Maritime_Southeast_Asia"),
    (23, "Philippines", "Maritime_Southeast_Asia"),
    (24, "Chile", "Latin_America"),
    (25, "Hungary", "Europe"),
    (26, "México", "Latin_America"),
    (27, "Thailand", "Mainland_Southeast_Asia"),
    (28, "Estonia", "Europe"),
    (29, "South Africa", "Africa"),
    (30, "Netherlands", "Europe"),
    (31, "Idelsk-Uralia", "Russia"),
    (32, "Serbia", "Europe"),
    (33, "Slovenia", "Europe"),
    (34, "Poland", "Europe"),
    (35, "Midwest Republic", "North_America"),
    (36, "Czechia", "Europe"),
    (37, "Slovakia", "Europe"),
    (38, "Romania", "Europe"),
    (39, "Lithuania", "Europe"),
    (40, "Bulgaria", "Europe"),
    (41, "Norway", "Europe"),
    (42, "Croatia", "Europe"),
    (43, "Finland", "Europe"),
    (44, "Demilitarized Zone (s. Ontario; not a nation)", "North_America"),
    (45, "Belarus", "Europe"),
    (46, "Latvia", "Europe"),
    (47, "Magna Lombardia", "Europe"),
    (48, "Colorado", "North_America"),
    (49, "Kazakhstan", "Central_Asia"),
    (50, "Uruguay", "Latin_America"),
    (51, "Quebec", "North_America"),
    (52, "Ukraine", "Europe"),
    (53, "Prairie Federation", "North_America"),
    (54, "Amazonia", "Latin_America"),
    (55, "Meridia", "Europe"),
    (56, "Siberia", "Russia"),
    (57, "Spain", "Europe"),
    (58, "Donska-Kubania", "Russia"),
    (59, "Sweden", "Europe"),
    (60, "Manchuria", "East_Asia"),
    (61, "Araucanía-Patagonia", "Latin_America"),
    (62, "Künnarantaiga", "Russia"),
    (63, "Mongolia", "East_Asia"),
    (64, "Yucatán", "Latin_America"),
    (65, "Northern Ireland", "Europe"),
    (66, "Denmark", "Europe"),
    (67, "East Turkestan", "East_Asia"),
    (68, "Sicilia (autonomous zone within Meridia)", "Europe"),
    (69, "Catalonia", "Europe"),
    (70, "West Papua", "Maritime_Southeast_Asia"),
    (71, "Aceh", "Maritime_Southeast_Asia"),
    (72, "Dagestan", "Russia"),
    (73, "Hawaii", "North_America"),
    (74, "Chechnya", "Russia"),
    (75, "Patani", "Mainland_Southeast_Asia"),
    (76, "Basque Country", "Europe"),
    (77, "Iceland", "Europe"),
    (78, "Kabardino-Balkaria", "Russia"),
    (79, "North Ossetia-Alania", "Russia"),
    (80, "Tibet", "East_Asia"),
    (81, "Ingushetia", "Russia"),
    (82, "Karachay-Cherkessia", "Russia"),
    (83, "Tuva", "Russia"),
]

# Signs: (number, name, concept_file)
SIGNS = [
    ("01 - Aries", "Aries", [
        "Self-assertion", "Identity", "Autonomy", "Initiative", "Beginning",
        "Courage", "Independence", "Anger", "Competition", "Recklessness",
    ]),
    ("02 - Taurus", "Taurus", [
        "Possession", "Ownership", "Self-worth", "Values", "Security",
        "Stability", "Wealth", "Possessiveness", "Stubbornness", "Sensuality",
    ]),
    ("03 - Gemini", "Gemini", [
        "Communication", "Information", "Learning", "Curiosity", "Connection",
        "Duality", "Siblings", "Mediation", "Gossip",
    ]),
    ("04 - Cancer", "Cancer", [
        "Home", "Family", "Belonging", "Nurture", "Protection",
        "Shelter", "Care", "Abandonment", "Motherhood",
    ]),
    ("05 - Leo", "Leo", [
        "Creativity", "Self-expression", "Pride", "Recognition", "Being seen",
        "Dignity", "Humiliation", "Generosity", "Leadership", "Play",
        "Honor", "Joy",
    ]),
    ("06 - Virgo", "Virgo", [
        "Work", "Service", "Usefulness", "Analysis", "Discernment",
        "Perfectionism", "Criticism", "Health", "Improvement",
    ]),
    ("07 - Libra", "Libra", [
        "Justice", "Fairness", "Partnership", "Balance", "Impartiality",
        "Diplomacy", "Reciprocity", "Indecision", "Peace at any price", "Projection",
    ]),
    ("08 - Scorpio", "Scorpio", [
        "Death", "Rebirth", "Purging", "Betrayal", "Control", "Trust",
        "Revenge", "Secrecy", "Power", "Crisis",
    ]),
    ("09 - Sagittarius", "Sagittarius", [
        "Faith", "Meaning", "Freedom", "Truth", "Belief", "Conviction",
        "Travel", "Honesty", "Education", "Fundamentalism",
    ]),
    ("10 - Capricorn", "Capricorn", [
        "Authority", "Duty", "Responsibility", "Discipline", "Ambition",
        "Hierarchy", "Merit", "Law", "Order",
    ]),
    ("11 - Aquarius", "Aquarius", [
        "Community", "Group", "Equality", "Reform", "Idealism", "Friendship",
        "Nonconformity", "Detachment", "Hope",
    ]),
    ("12 - Pisces", "Pisces", [
        "Compassion", "Empathy", "Self-sacrifice", "Dissolution", "Boundary",
        "Escapism", "Spirituality", "Surrender", "Intuition", "Crime", "Fear",
    ]),
]

# Build the INDEX.md content
lines = []
lines.append("# Hermes research: index")
lines.append("")
lines.append("One row per findings file. Hermes adds the row when it finishes a file; Claude adds the standing (see section 7 of `/home/kuroskalacs/Documents/Doll-Fi/media/HERMES_RULES.md`).")
lines.append("")
lines.append("## 1. Structure")
lines.append("")
lines.append("```")
lines.append("DCI findings root: /home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Hermes_research/findings/DCI_(Deep_Culture_Investigation)/")
lines.append("  INDEX.md (this file)")
lines.append("  <Continent>/          (e.g. North_America, Europe, East_Asia — 10 continents)")
lines.append("    <Country>/          (e.g. Cascadia, Japan, Germany — 83 countries)")
lines.append("      <Zodiac>/         (e.g. 01 - Aries, 02 - Taurus — 12 sign folders per country)")
lines.append("        <Concept>.md    (each concept finding file)")
lines.append("```")
lines.append("")
lines.append("## 2. Scale")
lines.append("")
lines.append("- **83 targets** (countries/cultures/nations) in Tepenia, from `DCI countries _ cultures checklist [Hermes].md` (Part C)")
lines.append("- **12 signs** (Zodiac meta-categories), from `Shared/Avenues/01 - 12 - Pisces.md` and the other 11 sign files")
lines.append("- **~10–12 concepts per sign** (varies by sign; see Section 3)")
lines.append("- **~9,960–10,000+ finding files** expected across all targets")
lines.append("")
lines.append("## 3. All 12 signs and their concepts")
lines.append("")
for num, name, concepts in SIGNS:
    lines.append(f"### {num} ({name}) ({len(concepts)} concepts)")
    lines.append(" | ".join(concepts))
    lines.append("")
lines.append("## 4. All 83 targets")
lines.append("")
lines.append("| # | Target | Continent | Status |")
lines.append("|---|---|---|---|")
for num, name, continent in TARGETS:
    lines.append(f"| {num} | {name} | {continent.replace('_', ' ')} | not started |")
lines.append("")
lines.append("## 5. Per-nation sign index (Cascadia — the pilot)")
lines.append("")
lines.append("> Only Cascadia has its per-nation index. All other nations follow the same template. This index is regenerated as files are created.")
lines.append("")
for num, name, concepts in SIGNS:
    lines.append(f"### {num} — done ({len(concepts)} files)")
    lines.append("| Concept file | Status |")
    lines.append("|---|---|")
    for concept in concepts:
        lines.append(f"| `{concept}.md` | UNREVIEWED |")
    lines.append("")
lines.append("## 6. Cross-reference: mapping the DCI concepts to Tepenia")
lines.append("")
lines.append("> The DCI concepts are applied to Tepenia's real-world-territory cultures. The `Shared/Avenues/` files contain the concept definitions. `Shared/Regional_Frameworks.md` contains the regional frameworks (Woodard for North America, etc.).")
lines.append("")
lines.append("## 7. Per-file notes")
lines.append("")
lines.append("> See section 7 of the universal rules in `/home/kuroskalacs/Documents/Doll-Fi/media/HERMES_RULES.md` for the standing conventions (UNREVIEWED → REVIEWED → READY flow, closing procedures, etc.).")
lines.append("")
lines.append("## 8. Sources")
lines.append("")
lines.append("- `DCI countries _ cultures checklist [Hermes].md` — target list (83 rows, Part C)")
lines.append("- `DCI research checklist [Hermes].md` — research checklist")
lines.append("- `Shared/Concept_Lists_by_Sign.md` — concept definitions per sign")
lines.append("- `Shared/Avenues/01 - 12 - Pisces.md` — concept files for all 12 signs")
lines.append("- `Shared/Regional_Frameworks.md` — regional frameworks (Woodard, etc.)")
lines.append("- `nations/World-Nations-Roster.md` — supplementary nation/culture roster (Tepenia)")
lines.append("")
content = "\n".join(lines)

# Write the INDEX.md
with open(os.path.join(DCI, "INDEX.md"), "w", encoding="utf-8") as f:
    f.write(content)

print(f"INDEX.md written: {len(content)} bytes, {content.count(chr(10)) + 1} lines")
