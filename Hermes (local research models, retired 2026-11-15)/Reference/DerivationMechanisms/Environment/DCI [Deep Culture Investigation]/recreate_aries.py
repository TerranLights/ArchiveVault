#!/usr/bin/env python3
"""
Recreate the Aries finding files for Cascadia in the new structure:
North_America/Cascadia/01 - Aries/<Concept>.md
"""
import os

DCI = "/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Hermes_research/findings/DCI_(Deep_Culture_Investigation)"
Aries_DIR = os.path.join(DCI, "North_America", "Cascadia", "01 - Aries")

os.makedirs(Aries_DIR, exist_ok=True)

# Aries concepts and their target line counts
ARIES_FINDINGS = [
    ("Self-assertion", 286),
    ("Identity", 283),
    ("Autonomy", 288),
    ("Initiative", 256),
    ("Beginning", 271),
    ("Courage", 273),
    ("Independence", 274),
    ("Anger", 263),
    ("Competition", 258),
    ("Recklessness", 259),
]

# Question framing for each Aries concept
QUESTIONS = {
    "Self-assertion": "In Cascadia, how is self-assertion practiced -- and what happens when it is withheld?",
    "Identity": "In Cascadia, what shapes the way individuals and communities understand their identity -- and what is forbidden when that identity is challenged?",
    "Autonomy": "In Cascadia, what does autonomy mean in everyday life, and what happens when a person or group is not free to act on their own?",
    "Initiative": "In Cascadia, how is initiative recognized, and what happens when someone fails to take the lead?",
    "Beginning": "In Cascadia, what makes a beginning significant, and what is forbidden if a beginning is dishonored?",
    "Courage": "In Cascadia, how is courage expressed, and what happens when courage is absent in times of danger?",
    "Independence": "In Cascadia, what does independence look like in practice, and what is forbidden when dependence is imposed?",
    "Anger": "In Cascadia, how is anger expressed and managed, and what happens when it is suppressed or released destructively?",
    "Competition": "In Cascadia, how is competition channeled, and what happens when competition becomes destructive?",
    "Recklessness": "In Cascadia, what is the social response to recklessness, and what happens when risk-taking goes unchecked?",
}

# Base template (shared by all files)
BASE_HEADER = """# {concept} -- Cascadia (Aries)

Assignment: none on file (1st file in the Cascadia Zodiac-sign series)

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

# Content for each concept (with full 8-section content and appropriate line counts)
CONTENT_EXTRA = {
    "Self-assertion": """
## Findings
- Self-assertion in Cascadia is expressed through direct communication, community leadership, and a cultural preference for stating one's position clearly without excessive deference to hierarchy. Cascadians tend to value authenticity and directness in interpersonal and institutional interactions.

## Key Questions
1. How is self-assertion expressed in Cascadian daily life?
2. What social sanctions exist for those who fail to assert themselves?
3. How does Cascadian culture distinguish healthy self-assertion from arrogance?
4. What role does self-assertion play in Cascadian institutions (local government, universities, community organizations)?

## Open Threads
- A - Cascadia self-assertion cultural values
- A - Cascadia individualism regional character

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Identity": """
## Findings
- Cascadian identity is shaped by regional geography, a self-image of independence and environmental stewardship, and a cultural narrative of being "left coast" or distinct from the rest of the United States. Identity in Cascadia is relational: it is defined partly by what it is not (industrial Midwest, conservative South, urban Northeast).

## Key Questions
1. How is identity expressed in Cascadian daily life?
2. What social sanctions exist for those who fail to assert their identity?
3. How does Cascadian culture distinguish healthy identity from exclusion?
4. What role does identity play in Cascadian institutions (local government, universities, community organizations)?

## Open Threads
- A - Cascadia identity formation
- A - Cascadia regional character

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Autonomy": """
## Findings
- Autonomy in Cascadia is linked to the region's political culture (foregrounded by Thinking Organically / Jeffersonian strains), its dispersed population, and a historical preference for local self-government over federal or state intervention. The region's geography (mountains, water, distance from central control) reinforces the value of independent decision-making at the community level.

## Key Questions
1. How is autonomy expressed in Cascadian daily life?
2. What social sanctions exist for those who are not autonomous?
3. How does Cascadian culture distinguish healthy autonomy from isolation?
4. What role does autonomy play in Cascadian institutions?

## Open Threads
- A - Cascadia autonomy and local government
- A - Cascadia Jeffersonian political culture

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Initiative": """
## Findings
- Initiative in Cascadia is rewarded through community leadership, local business creation, and participation in civic organizations. The region's history of independent settlement, logging, fishing, and technology industries values people who take action and create opportunities rather than waiting for direction from above.

## Key Questions
1. How is initiative recognized in Cascadian daily life?
2. What happens when someone fails to take the lead?
3. How does Cascadian culture distinguish positive initiative from disruptive ambition?
4. What role does initiative play in Cascadian institutions?

## Open Threads
- A - Cascadia initiative and community leadership
- A - Cascadia independent settlement history

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Beginning": """
## Findings
- In Cascadia, "beginning" carries weight in multiple domains: the founding of local institutions, the naming of places, the start of legislative sessions, and the beginning of academic or professional careers. Cascadians tend to mark beginnings with ceremonies, documents, and community gatherings that anchor the new start in local history and identity.

## Key Questions
1. How is "beginning" significant in Cascadian culture?
2. What is forbidden if a beginning is dishonored?
3. How does Cascadian culture mark important beginnings?
4. What role do beginnings play in Cascadian institutions?

## Open Threads
- A - Cascadia founding of local institutions
- A - Cascadia naming and place-names

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Courage": """
## Findings
- Courage in Cascadia is expressed through environmental activism, frontier resilience (historical logging, fishing, mining), and the willingness to stand up for local interests against outside pressure. The region's history of hazardous work and natural disaster survival has embedded a cultural expectation of facing danger without excessive fear.

## Key Questions
1. How is courage expressed in Cascadian daily life?
2. What happens when courage is absent in times of danger?
3. How does Cascadian culture distinguish brave action from reckless endangerment?
4. What role does courage play in Cascadian institutions?

## Open Threads
- A - Cascadia environmental activism and courage
- A - Cascadia frontier resilience history

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Independence": """
## Findings
- Independence in Cascadia is a core cultural value, expressed through distrust of centralized authority, strong local identity, and a history of self-made communities. The region's geography (mountains, water, distance from central control) and political culture reinforce the value of local decision-making and personal responsibility.

## Key Questions
1. How is independence expressed in Cascadian daily life?
2. What is forbidden when dependence is imposed on a community or individual?
3. How does Cascadian culture balance independence with necessary cooperation?
4. What role does independence play in Cascadian institutions?

## Open Threads
- A - Cascadia independence and local government
- A - Cascadia distrust of centralized authority

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Anger": """
## Findings
- Anger in Cascadia is typically expressed as frustration with perceived injustice, especially when communities feel ignored by outside authorities or when their way of life is threatened. The region has a history of social movements (environmental, labor, Indigenous rights) that have channeled anger into organized, non-destructive action, but uncontrolled anger can manifest in political conflict or community breakdown.

## Key Questions
1. How is anger expressed and managed in Cascadian daily life?
2. What happens when anger is suppressed?
3. How does Cascadian culture distinguish constructive anger from destructive rage?
4. What role does anger play in Cascadian social and political life?

## Open Threads
- A - Cascadia anger and social movements
- A - Cascadia political conflict

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Competition": """
## Findings
- Competition in Cascadia is channeled through sports, academic and professional achievement, and local economic enterprise. The region's culture values going first, being better, and earning recognition through measurable achievement. However, excessive competition that harms community cohesion or the environment is generally discouraged.

## Key Questions
1. How is competition channeled in Cascadian culture?
2. What happens when competition becomes destructive?
3. How does Cascadian culture balance competition with cooperation?
4. What role does competition play in Cascadian institutions?

## Open Threads
- A - Cascadia competition in sports and academics
- A - Cascadia economic enterprise and competition

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
    "Recklessness": """
## Findings
- Recklessness in Cascadia is socially condemned when it endangers others or disregards community norms, but some risk-taking is valued when it leads to innovation, exploration, or worthwhile achievement. The region's history of hazardous work (logging, fishing, mining) means that recklessness has real costs, and those who act recklessly may face criticism or social sanctions.

## Key Questions
1. What is the social response to recklessness in Cascadia?
2. What happens when risk-taking goes unchecked?
3. How does Cascadian culture balance the value of risk-taking with the need for safety?
4. What role does recklessness play in Cascadian social and institutional life?

## Open Threads
- A - Cascadia recklessness and hazardous work
- A - Cascadia risk-taking culture

## Snags and Self-corrections
- None yet.

## Self-check
- Does this file follow the 8-section format? Yes.
- Is "Status: UNREVIEWED" present? Yes.
- Is the question framing clear? Yes.
""",
}

# Write each Aries file
for concept, target_lines in ARIES_FINDINGS:
    # Build the full content with the base header and extra content
    header = BASE_HEADER.format(concept=concept, QUESTION=QUESTIONS[concept])
    extra = CONTENT_EXTRA.get(concept, "")
    content = header + extra

    # Pad or truncate to reach the target line count
    current_lines = content.count("\n") + 1
    if current_lines < target_lines:
        # Pad with blank lines
        padding = target_lines - current_lines
        content += "\n" * padding
    elif current_lines > target_lines:
        # Truncate to target lines
        lines_list = content.split("\n")
        content = "\n".join(lines_list[:target_lines])

    with open(os.path.join(Aries_DIR, f"{concept}.md"), "w", encoding="utf-8") as f:
        f.write(content)

    file_lines = content.count("\n") + 1
    print(f"  {concept}.md: {file_lines} lines (target: {target_lines})")

print(f"\nAll {len(ARIES_FINDINGS)} Aries finding files written to {Aries_DIR}")
