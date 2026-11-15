#!/usr/bin/env python3
"""
Restructure DCI findings folders from:
  findings/DCI_(Deep_Culture_Investigation)/<Target>/<Zodiac>/<Finding>.md
to:
  findings/DCI_(Deep_Culture_Investigation)/<Continent>/<Country>/<Zodiac>/<Finding>.md

The 83 target folders are currently directly under the findings root.
The 12 zodiac folders (01 - Aries ... 12 - Pisces) already exist inside each
target folder.

Strategy:
  1. Read the checklist Part C to get exact target names (with numbers).
  2. Map each target name to a continent folder.
  3. Create continent folders.
  4. Create country folders (using the target name as the folder name).
  5. Move each target folder into its continent folder.
"""
import os
import re
import shutil

ROOT = "/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Hermes_research/findings"
DCI = os.path.join(ROOT, "DCI_(Deep_Culture_Investigation)")

# Target name (as in checklist) -> continent folder name
TARGET_TO_CONTINENT = {
    # North America (12)
    "Cascadia": "North_America",
    "Alaska": "North_America",
    "Sonora": "North_America",
    "CSA": "North_America",
    "Appalachia": "North_America",
    "New England": "North_America",
    "Midwest Republic": "North_America",
    "Prairie Federation": "North_America",
    "Quebec": "North_America",
    "Colorado": "North_America",
    "Demilitarized Zone (s. Ontario; not a nation)": "North_America",
    "Hawaii": "North_America",

    # Latin America (8)
    "Brazil": "Latin_America",
    "Argentina (without Patagonia)": "Latin_America",
    "Chile": "Latin_America",
    "Uruguay": "Latin_America",
    "México": "Latin_America",
    "Yucatán": "Latin_America",
    "Amazonia": "Latin_America",
    "Araucanía-Patagonia": "Latin_America",

    # East Asia (8)
    "Korea": "East_Asia",
    "Sinian Federation": "East_Asia",
    "Japan": "East_Asia",
    "Taiwan": "East_Asia",
    "Manchuria": "East_Asia",
    "Mongolia": "East_Asia",
    "Tibet": "East_Asia",
    "East Turkestan": "East_Asia",

    # Mainland Southeast Asia (3)
    "Vietnam": "Mainland_Southeast_Asia",
    "Thailand": "Mainland_Southeast_Asia",
    "Patani": "Mainland_Southeast_Asia",

    # Maritime Southeast Asia (5)
    "Indonesia": "Maritime_Southeast_Asia",
    "Malaysia": "Maritime_Southeast_Asia",
    "Philippines": "Maritime_Southeast_Asia",
    "West Papua": "Maritime_Southeast_Asia",
    "Aceh": "Maritime_Southeast_Asia",

    # Russia (12)
    "Russia (core state)": "Russia",
    "Idelsk-Uralia": "Russia",
    "Siberia": "Russia",
    "Donska-Kubania": "Russia",
    "Künnarantaiga": "Russia",
    "Chechnya": "Russia",
    "Dagestan": "Russia",
    "Ingushetia": "Russia",
    "Kabardino-Balkaria": "Russia",
    "North Ossetia-Alania": "Russia",
    "Karachay-Cherkessia": "Russia",
    "Tuva": "Russia",

    # Central Asia (1)
    "Kazakhstan": "Central_Asia",

    # Oceania (2)
    "Australia": "Oceania",
    "New Zealand": "Oceania",

    # Africa (1)
    "South Africa": "Africa",

    # Europe (31)
    "United Kingdom": "Europe",
    "Germany": "Europe",
    "France": "Europe",
    "Austro-Bavaria": "Europe",
    "Magna Lombardia": "Europe",
    "Meridia": "Europe",
    "Spain": "Europe",
    "Sweden": "Europe",
    "Northern Ireland": "Europe",
    "Denmark": "Europe",
    "Sicilia (autonomous zone within Meridia)": "Europe",
    "Catalonia": "Europe",
    "Basque Country": "Europe",
    "Iceland": "Europe",
    "Hungary": "Europe",
    "Estonia": "Europe",
    "Netherlands": "Europe",
    "Serbia": "Europe",
    "Slovenia": "Europe",
    "Poland": "Europe",
    "Czechia": "Europe",
    "Slovakia": "Europe",
    "Romania": "Europe",
    "Lithuania": "Europe",
    "Bulgaria": "Europe",
    "Norway": "Europe",
    "Croatia": "Europe",
    "Finland": "Europe",
    "Belarus": "Europe",
    "Latvia": "Europe",
    "Ukraine": "Europe",
}

# Get the list of targets from the checklist
CHECKLIST = "/home/kuroskalacs/Documents/Doll-Fi/media/DCI countries _ cultures checklist [Hermes].md"
targets = []
with open(CHECKLIST, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()
in_part_c = False
for line in lines:
    if line.strip() == "# Part C · The targets":
        in_part_c = True
        continue
    if in_part_c:
        # Match table rows like "| 1 | Cascadia | 403,029 | North America | ... |"
        m = re.match(r'\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|', line)
        if m:
            num = m.group(1)
            target = m.group(2).strip()
            targets.append((num, target))

print("Targets found in checklist:", len(targets))
for num, target in targets:
    print(f"  {num}: {target}")

# Build mapping: target name -> continent folder name
target_to_continent = {}
for num, target in targets:
    continent = TARGET_TO_CONTINENT.get(target)
    if continent is None:
        print(f"WARNING: target '{target}' (#{num}) not in TARGET_TO_CONTINENT mapping")
    target_to_continent[target] = continent

# Find current target folders on disk
current_folders = []
for entry in os.listdir(DCI):
    full = os.path.join(DCI, entry)
    if os.path.isdir(full):
        current_folders.append(entry)

print(f"\nCurrent target folders on disk: {len(current_folders)}")
for f in sorted(current_folders):
    print(f"  {f}")

# Verify all current folders are in the mapping
unmapped = [f for f in current_folders if f not in target_to_continent]
if unmapped:
    print("\nWARNING: folders on disk not in TARGET_TO_CONTINENT:")
    for f in unmapped:
        print(f"  {f}")
else:
    print("\nAll current folders are mapped to continents.")

# Do the restructure
print("\n=== STARTING RESTRUCTURE ===")
for folder in sorted(current_folders):
    if folder not in target_to_continent:
        print(f"Skipping unknown folder: {folder}")
        continue
    continent = target_to_continent[folder]
    new_continent_path = os.path.join(DCI, continent)
    new_country_path = os.path.join(new_continent_path, folder)
    old_path = os.path.join(DCI, folder)

    # Create continent folder if needed
    if not os.path.isdir(new_continent_path):
        os.makedirs(new_continent_path)
        print(f"  Created continent folder: {continent}/")

    # Create country folder
    os.makedirs(new_country_path, exist_ok=True)

    # Move contents from old folder to new country folder
    if os.path.isdir(old_path):
        for item in os.listdir(old_path):
            shutil.move(os.path.join(old_path, item), new_country_path)
        os.rmdir(old_path)
        print(f"  Moved {folder}/ -> {continent}/{folder}/")

print("=== RESTRUCTURE COMPLETE ===")

# Verify
print("\n=== VERIFICATION ===")
for entry in sorted(os.listdir(DCI)):
    full = os.path.join(DCI, entry)
    if os.path.isdir(full):
        countries = os.listdir(full)
        print(f"{entry}/ -> {len(countries)} country folders: {sorted(countries)}")
