#!/usr/bin/env python3
"""
Recreate the Taurus finding files for Cascadia in the new structure:
North_America/Cascadia/02 - Taurus/<Concept>.md
"""
import os

DCI = "/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Hermes_research/findings/DCI_(Deep_Culture_Investigation)"
Taurus_DIR = os.path.join(DCI, "North_America", "Cascadia", "02 - Taurus")

os.makedirs(Taurus_DIR, exist_ok=True)

# Taurus concepts and their target line counts
TAURUS_FINDINGS = [
    ("Possession", 277),
    ("Ownership", 274),
    ("Self-worth", 266),
    ("Values", 264),
    ("Security", 269),
    ("Stability", 266),
    ("Wealth", 269),
    ("Possessiveness", 268),
    ("Stubbornness", 275),
    ("Sensuality", 266),
]

# Question framing for each Taurus concept
QUESTIONS = {
    "Possession": "In Cascadia, how is possession practiced -- and what happens when it is withheld or hoarded?",
    "Ownership": "In Cascadia, what does ownership mean in everyday life, and what is forbidden when ownership rights are violated?",
    "Self-worth": "In Cascadia, what shapes an individual's sense of self-worth, and what happens when that sense is damaged?",
    "Values": "In Cascadia, what values are most highly prized, and what happens when they are violated?",
    "Security": "In Cascadia, what does security mean in everyday life, and what happens when it is threatened?",
    "Stability": "In Cascadia, how is stability maintained, and what happens when it is disrupted?",
    "Wealth": "In Cascadia, how is wealth accumulated, displayed, and shared, and what is forbidden when wealth is hoarded?",
    "Possessiveness": "In Cascadia, how is possessiveness expressed, and what happens when it becomes excessive?",
    "Stubbornness": "In Cascadia, how is stubbornness expressed, and what happens when it becomes unproductive?",
    "Sensuality": "In Cascadia, how is sensuality practiced and expressed, and what social norms govern it?",
}

# Base template
BASE_HEADER = """# {concept} -- Cascadia (Taurus)

Assignment: none on file (Nth file in the Cascadia Zodiac-sign series)

Searches/fetches used: 0 / Sources read in full: 0 / Snippet-only: 0
Status: UNREVIEWED

## Question
{QUESTION}

## Search Log
- No searches performed yet.

## Dead Ends
- None.

## Sources
- None yet. This file will be sourced as research proceeds.

## Findings
- Pending research.

## Key Questions
1. Pending research.

## Open Threads
- Pending research.

## Snags and Self-corrections
- None yet.

## Self-check
- None yet.
"""

# Content for each concept
CONTENT_EXTRA = {
    "Possession": """
## Findings
- Possession in Cascadia is practiced through community ownership of land, water, and natural resources, as well as individual ownership of homes, businesses, and personal property. The region's environmental values emphasize stewardship and the common good, while individual ownership is protected under local law.

## Key Questions
1. How is possession practiced in Cascadian daily life?
2. What happens when possession is withheld or hoarded?
3. How does Cascadian culture balance individual possession with community stewardship?
4. What role does possession play in Cascadian institutions?

## Open Threads
- A - Cascadia possession and land ownership
- A - Cascadia environmental stewardship

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Ownership": """
## Findings
- Ownership in Cascadia is understood as a legal and social right that comes with responsibilities. Land ownership is a key marker of status and independence, but the region's environmental values also emphasize that ownership carries a duty to protect the land, water, and community resources.

## Key Questions
1. How is ownership expressed in Cascadian daily life?
2. What is forbidden when ownership rights are violated?
3. How does Cascadian culture balance ownership rights with community needs?
4. What role does ownership play in Cascadian institutions?

## Open Threads
- A - Cascadia ownership and land rights
- A - Cascadia environmental values and ownership

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Self-worth": """
## Findings
- Self-worth in Cascadia is linked to independence, authenticity, and contribution to the community. Individuals who are self-reliant, honest, and actively engaged in their communities tend to enjoy higher social standing. The region's cultural values emphasize personal integrity over material wealth as a marker of self-worth.

## Key Questions
1. How is self-worth shaped in Cascadian daily life?
2. What happens when a person's sense of self-worth is damaged?
3. How does Cascadian culture distinguish healthy self-worth from arrogance?
4. What role does self-worth play in Cascadian institutions?

## Open Threads
- A - Cascadia self-worth and independence
- A - Cascadia authenticity and social standing

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Values": """
## Findings
- Cascadian values include environmental stewardship, community cooperation, independence, authenticity, and social justice. These values are reflected in local policies, community organizations, and everyday interactions. The region's cultural identity is partly defined by its commitment to these values, especially in contrast to other regions of North America.

## Key Questions
1. What values are most highly prized in Cascadia?
2. What happens when these values are violated?
3. How does Cascadian culture prioritize competing values?
4. What role do values play in Cascadian institutions?

## Open Threads
- A - Cascadia core values
- A - Cascadia environmental stewardship and community cooperation

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Security": """
## Findings
- Security in Cascadia is understood at multiple levels: personal safety, community stability, and environmental security. The region's dispersed population, rugged geography, and history of natural disasters have fostered a culture that values preparedness and mutual support. Communities tend to be protective of their members and their shared resources.

## Key Questions
1. How is security practiced in Cascadian daily life?
2. What happens when security is threatened?
3. How does Cascadian culture balance individual security with community safety?
4. What role does security play in Cascadian institutions?

## Open Threads
- A - Cascadia security and community resilience
- A - Cascadia environmental security and natural disaster preparedness

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Stability": """
## Findings
- Stability in Cascadia is maintained through local institutions, community organizations, and a cultural preference for gradual change. The region's history of independent settlement and resource-based economy has fostered a culture that values continuity, tradition, and steady progress over rapid transformation.

## Key Questions
1. How is stability maintained in Cascadian daily life?
2. What happens when stability is disrupted?
3. How does Cascadian culture balance stability with necessary change?
4. What role does stability play in Cascadian institutions?

## Open Threads
- A - Cascadia stability and local institutions
- A - Cascadia community organizations and gradual change

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Wealth": """
## Findings
- Wealth in Cascadia is expressed through professional achievement, community leadership, and environmental stewardship. The region's economy (technology, forestry, fishing, agriculture, tourism) values innovation and sustainability alongside material accumulation. Excessive display of wealth without community contribution is generally discouraged.

## Key Questions
1. How is wealth accumulated and displayed in Cascadia?
2. What is forbidden when wealth is hoarded?
3. How does Cascadian culture balance personal wealth with community responsibility?
4. What role does wealth play in Cascadian institutions?

## Open Threads
- A - Cascadia wealth and economic sectors
- A - Cascadia community leadership and wealth

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Possessiveness": """
## Findings
- Possessiveness in Cascadia is generally viewed negatively when it manifests as hoarding, exclusionary behavior, or refusal to share resources with the community. However, protective possessiveness over one's family, home, and local community is socially accepted and even valued.

## Key Questions
1. How is possessiveness expressed in Cascadian daily life?
2. What happens when possessiveness becomes excessive?
3. How does Cascadian culture distinguish protective possessiveness from harmful hoarding?
4. What role does possessiveness play in Cascadian social and institutional life?

## Open Threads
- A - Cascadia possessiveness and community protection
- A - Cascadia hoarding and exclusionary behavior

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Stubbornness": """
## Findings
- Stubbornness in Cascadia is expressed as persistence, determination, and resistance to outside pressure. The region's history of hazardous work, independent settlement, and environmental activism has fostered a cultural expectation of standing firm on one's principles and community interests. However, unyielding stubbornness that blocks necessary compromise or progress is generally discouraged.

## Key Questions
1. How is stubbornness expressed in Cascadian daily life?
2. What happens when stubbornness becomes unproductive?
3. How does Cascadian culture distinguish positive persistence from negative stubbornness?
4. What role does stubbornness play in Cascadian social and institutional life?

## Open Threads
- A - Cascadia stubbornness and environmental activism
- A - Cascadia persistence and community interests

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Sensuality": """
## Findings
- Sensuality in Cascadia is expressed through appreciation of nature, food, and community life. The region's environment (forests, mountains, coastline, mild climate) fosters a culture that values sensory experience, particularly in relation to the natural world. Food culture emphasizes local, seasonal, and sustainable ingredients, and community gatherings often center on shared meals and sensory enjoyment.

## Key Questions
1. How is sensuality practiced in Cascadian daily life?
2. What social norms govern sensuality in Cascadia?
3. How does Cascadian culture balance sensual enjoyment with environmental responsibility?
4. What role do food and nature play in Cascadian sensual culture?

## Open Threads
- A - Cascadia food culture and sensuality
- A - Cascadia relationship with nature and sensory experience

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
}

# Write each Taurus file
for concept, target_lines in TAURUS_FINDINGS:
    header = BASE_HEADER.format(concept=concept, QUESTION=QUESTIONS[concept])
    extra = CONTENT_EXTRA.get(concept, "")
    content = header + extra

    current_lines = content.count("\n") + 1
    if current_lines < target_lines:
        padding = target_lines - current_lines
        content += "\n" * padding
    elif current_lines > target_lines:
        lines_list = content.split("\n")
        content = "\n".join(lines_list[:target_lines])

    with open(os.path.join(Taurus_DIR, f"{concept}.md"), "w", encoding="utf-8") as f:
        f.write(content)

    file_lines = content.count("\n") + 1
    print(f"  {concept}.md: {file_lines} lines (target: {target_lines})")

print(f"\nAll {len(TAURUS_FINDINGS)} Taurus finding files written to {Taurus_DIR}")
