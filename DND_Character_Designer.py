import random

races = ("Human", "Aarakocra (birdfolk)", "Aasimar (celestial blood)", "Autognome (robot)", "Bugbear",
         "Bullywug (frogfolk)", "Centaur (half human, half horse)", "Changeling (doppelganger-kin)",
         "Dhampir (half human, half vampire)", "Dragonborn (Black Dragon Ancestry)",
         "Dragonborn (Blue Dragon Ancestry)", "Dragonborn (Brass Dragon Ancestry)",
         "Dragonborn (Bronze Dragon Ancestry)", "Dragonborn (Copper Dragon Ancestry)",
         "Dragonborn (Gold Dragon Ancestry)", "Dragonborn (Green Dragon Ancestry)",
         "Dragonborn (Red Dragon Ancestry)", "Dragonborn (Silver Dragon Ancestry)",
         "Dragonborn (White Dragon Ancestry)", "Dwarf (Duergar)", "Dwarf (Hill Dwarf)", "Dwarf (Mountain Dwarf)",
         "Eladrin (Feywild Elf)", "Elf (Astral Elf)", "Elf (Dark Elf/Drow)", "Elf (High Elf)", "Elf (Sea Elf)",
         "Elf (Shadow Elf/Shadar-kai)", "Elf (Wood Elf)", "Fairy (feyfolk)", "Firbolg (forest giant)",
         "Genasi (air genie kin)", "Genasi (earth genie kin)", "Genasi (fire genie kin)", "Genasi (water genie kin)",
         "Gith (Githyanki)", "Gith (Githzerai)", "Gnome (Deep Gnome/Svirfneblin)", "Gnome (Forest Gnome)",
         "Gnome (Rock Gnome)", "Goblin", "Goliath", "Grung (frogfolk)", "Half-Elf", "Half-Orc", "Halfling (Ghostwise)",
         "Halfling (Lightfoot)", "Halfling (Stout)", "Harengon (rabbitfolk)", "Hobgoblin", "Kalashtar",
         "Kenku (crowfolk)", "Kobold", "Leonin (lionfolk)", "Lizardfolk", "Loxodon (elephantfolk)", "Minotaur",
         "Orc", "Owlin (owlfolk)", "Satyr", "Shifter (beastfolk)", "Tabaxi (catfolk)", "Thri-kreen (mantisfolk)",
         "Tiefling (infernal blood)", "Tortle (turtlefolk)", "Triton (sea dweller)", "Warforged (living construct)",
         "Yuan-ti Pureblood (snakefolk)")

classes = ("Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger",
           "Rogue", "Sorcerer", "Warlock", "Wizard")

genders = ("Male", "Female")
base_ac = 10

random_race = random.choice(races)
random_class = random.choice(classes)
random_gender = random.choice(genders)
random_lvl = random.randint(1, 20)

score_roll = random.randint(1, 6)
score_roll_2 = random.randint(1, 6)
score_roll_3 = random.randint(1, 6)
score_roll_4 = random.randint(1, 6)
score_rolls = [score_roll, score_roll_2, score_roll_3, score_roll_4]
lowest_score_roll = min(score_rolls)
score_rolls.remove(lowest_score_roll)
ability_score_str = sum(score_rolls)

score_roll = random.randint(1, 6)
score_roll_2 = random.randint(1, 6)
score_roll_3 = random.randint(1, 6)
score_roll_4 = random.randint(1, 6)
score_rolls = [score_roll, score_roll_2, score_roll_3, score_roll_4]
lowest_score_roll = min(score_rolls)
score_rolls.remove(lowest_score_roll)
ability_score_dex = sum(score_rolls)

score_roll = random.randint(1, 6)
score_roll_2 = random.randint(1, 6)
score_roll_3 = random.randint(1, 6)
score_roll_4 = random.randint(1, 6)
score_rolls = [score_roll, score_roll_2, score_roll_3, score_roll_4]
lowest_score_roll = min(score_rolls)
score_rolls.remove(lowest_score_roll)
ability_score_con = sum(score_rolls)

score_roll = random.randint(1, 6)
score_roll_2 = random.randint(1, 6)
score_roll_3 = random.randint(1, 6)
score_roll_4 = random.randint(1, 6)
score_rolls = [score_roll, score_roll_2, score_roll_3, score_roll_4]
lowest_score_roll = min(score_rolls)
score_rolls.remove(lowest_score_roll)
ability_score_int = sum(score_rolls)

score_roll = random.randint(1, 6)
score_roll_2 = random.randint(1, 6)
score_roll_3 = random.randint(1, 6)
score_roll_4 = random.randint(1, 6)
score_rolls = [score_roll, score_roll_2, score_roll_3, score_roll_4]
lowest_score_roll = min(score_rolls)
score_rolls.remove(lowest_score_roll)
ability_score_wis = sum(score_rolls)

score_roll = random.randint(1, 6)
score_roll_2 = random.randint(1, 6)
score_roll_3 = random.randint(1, 6)
score_roll_4 = random.randint(1, 6)
score_rolls = [score_roll, score_roll_2, score_roll_3, score_roll_4]
lowest_score_roll = min(score_rolls)
score_rolls.remove(lowest_score_roll)
ability_score_cha = sum(score_rolls)

# Define racial bonuses
ability_score_str_bonus = 0
ability_score_dex_bonus = 0
ability_score_con_bonus = 0
ability_score_int_bonus = 0
ability_score_wis_bonus = 0
ability_score_cha_bonus = 0

# Apply racial bonuses based on chosen race
if random_race == "Human":
    ability_score_str_bonus += 1
    ability_score_dex_bonus += 1
    ability_score_con_bonus += 1
    ability_score_int_bonus += 1
    ability_score_wis_bonus += 1
    ability_score_cha_bonus += 1
elif random_race == "Aarakocra (birdfolk)":
    ability_score_dex_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Aasimar (celestial blood)":
    ability_score_cha_bonus += 2
    ability_score_wis_bonus += 1  # Change if subraces are considered
elif random_race == "Autognome (robot)":
    ability_score_con_bonus += 2
    ability_score_int_bonus += 1  # Choice can be changed
elif random_race == "Bugbear":
    ability_score_str_bonus += 2
    ability_score_dex_bonus += 1
elif random_race == "Bullywug (frogfolk)":
    ability_score_con_bonus += 2
    ability_score_dex_bonus += 1
elif random_race == "Centaur (half human, half horse)":
    ability_score_str_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Changeling (doppelganger-kin)":
    ability_score_cha_bonus += 2
    ability_score_dex_bonus += 1  # Choice can be changed
elif random_race == "Dhampir (half human, half vampire)":
    ability_score_dex_bonus += 2
    ability_score_cha_bonus += 1  # Choice can be changed
elif "Dragonborn" in random_race:
    ability_score_str_bonus += 2
    ability_score_cha_bonus += 1
elif random_race == "Dwarf (Duergar)":
    ability_score_con_bonus += 2
    ability_score_str_bonus += 1
elif random_race == "Dwarf (Hill Dwarf)":
    ability_score_con_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Dwarf (Mountain Dwarf)":
    ability_score_con_bonus += 2
    ability_score_str_bonus += 2
elif random_race == "Eladrin (Feywild Elf)":
    ability_score_dex_bonus += 2
    ability_score_cha_bonus += 1
elif random_race == "Elf (Astral Elf)":
    ability_score_dex_bonus += 2
    ability_score_int_bonus += 1
elif random_race == "Elf (Dark Elf/Drow)":
    ability_score_dex_bonus += 2
    ability_score_cha_bonus += 1
elif random_race == "Elf (High Elf)":
    ability_score_dex_bonus += 2
    ability_score_int_bonus += 1
elif random_race == "Elf (Sea Elf)":
    ability_score_dex_bonus += 2
    ability_score_con_bonus += 1
elif random_race == "Elf (Shadow Elf/Shadar-kai)":
    ability_score_dex_bonus += 2
    ability_score_con_bonus += 1
elif random_race == "Elf (Wood Elf)":
    ability_score_dex_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Fairy (feyfolk)":
    ability_score_dex_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Firbolg (forest giant)":
    ability_score_wis_bonus += 2
    ability_score_str_bonus += 1
elif random_race == "Genasi (air genie kin)":
    ability_score_con_bonus += 2
    ability_score_dex_bonus += 1
elif random_race == "Genasi (earth genie kin)":
    ability_score_con_bonus += 2
    ability_score_str_bonus += 1
elif random_race == "Genasi (fire genie kin)":
    ability_score_con_bonus += 2
    ability_score_int_bonus += 1
elif random_race == "Genasi (water genie kin)":
    ability_score_con_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Gith (Githyanki)":
    ability_score_str_bonus += 2
    ability_score_int_bonus += 1
elif random_race == "Gith (Githzerai)":
    ability_score_wis_bonus += 2
    ability_score_int_bonus += 1
elif random_race == "Gnome (Deep Gnome/Svirfneblin)":
    ability_score_int_bonus += 2
    ability_score_dex_bonus += 1
elif random_race == "Gnome (Forest Gnome)":
    ability_score_int_bonus += 2
    ability_score_dex_bonus += 1
elif random_race == "Gnome (Rock Gnome)":
    ability_score_int_bonus += 2
    ability_score_con_bonus += 1
elif random_race == "Goblin":
    ability_score_dex_bonus += 2
    ability_score_con_bonus += 1
elif random_race == "Goliath":
    ability_score_str_bonus += 2
    ability_score_con_bonus += 1
elif random_race == "Grung (frogfolk)":
    ability_score_dex_bonus += 2
    ability_score_con_bonus += 1
elif random_race == "Half-Elf":
    ability_score_cha_bonus += 2
    ability_score_dex_bonus += 1  # Choice can be changed
    ability_score_con_bonus += 1  # Choice can be changed
elif random_race == "Half-Orc":
    ability_score_str_bonus += 2
    ability_score_con_bonus += 1
elif random_race == "Halfling (Ghostwise)":
    ability_score_dex_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Halfling (Lightfoot)":
    ability_score_dex_bonus += 2
    ability_score_cha_bonus += 1
elif random_race == "Halfling (Stout)":
    ability_score_dex_bonus += 2
    ability_score_con_bonus += 1
elif random_race == "Harengon (rabbitfolk)":
    ability_score_dex_bonus += 2
    ability_score_wis_bonus += 1  # Choice can be changed
elif random_race == "Hobgoblin":
    ability_score_con_bonus += 2
    ability_score_int_bonus += 1
elif random_race == "Kalashtar":
    ability_score_wis_bonus += 2
    ability_score_cha_bonus += 1
elif random_race == "Kenku (crowfolk)":
    ability_score_dex_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Kobold":
    ability_score_dex_bonus += 2
    ability_score_cha_bonus += 1
elif random_race == "Leonin (lionfolk)":
    ability_score_con_bonus += 2
    ability_score_str_bonus += 1
elif random_race == "Lizardfolk":
    ability_score_con_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Loxodon (elephantfolk)":
    ability_score_con_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Minotaur":
    ability_score_str_bonus += 2
    ability_score_con_bonus += 1
elif random_race == "Orc":
    ability_score_str_bonus += 2
    ability_score_con_bonus += 1
elif random_race == "Owlin (owlfolk)":
    ability_score_dex_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Satyr":
    ability_score_cha_bonus += 2
    ability_score_dex_bonus += 1
elif random_race == "Shifter (beastfolk)":
    ability_score_dex_bonus += 2
    ability_score_wis_bonus += 1  # Choice can be changed
elif random_race == "Tabaxi (catfolk)":
    ability_score_dex_bonus += 2
    ability_score_cha_bonus += 1
elif random_race == "Thri-kreen (mantisfolk)":
    ability_score_dex_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Tiefling (infernal blood)":
    ability_score_cha_bonus += 2
    ability_score_int_bonus += 1
elif random_race == "Tortle (turtlefolk)":
    ability_score_str_bonus += 2
    ability_score_wis_bonus += 1
elif random_race == "Triton (sea dweller)":
    ability_score_str_bonus += 1
    ability_score_con_bonus += 1
    ability_score_cha_bonus += 1
elif random_race == "Warforged (living construct)":
    ability_score_con_bonus += 2
    ability_score_int_bonus += 1  # Choice can be changed
elif random_race == "Yuan-ti Pureblood (snakefolk)":
    ability_score_cha_bonus += 2
    ability_score_int_bonus += 1

# Calculate modifiers
str_modifier = (ability_score_str - 10) // 2
dex_modifier = (ability_score_dex - 10) // 2
con_modifier = (ability_score_con - 10) // 2
int_modifier = (ability_score_int - 10) // 2
wis_modifier = (ability_score_wis - 10) // 2
cha_modifier = (ability_score_cha - 10) // 2

# Calculate hit points (HP)
hit_dice = {
    "Artificer": 8,
    "Barbarian": 12,
    "Bard": 8,
    "Cleric": 8,
    "Druid": 8,
    "Fighter": 10,
    "Monk": 8,
    "Paladin": 10,
    "Ranger": 10,
    "Rogue": 8,
    "Sorcerer": 6,
    "Warlock": 8,
    "Wizard": 6
}

hit_die_max = hit_dice[random_class]

hp = hit_die_max + con_modifier
for level in range(2, random_lvl + 1):
    hp += random.randint(1, hit_die_max) + con_modifier

# Calculate Armor Class (AC)
if ability_score_dex >= 10:
    ac = base_ac + dex_modifier
else:
    ac = base_ac

starting_equipment = {
    "Artificer": ["Tools", "Potion of Healing", "Light Crossbow", "20 Bolts"],
    "Barbarian": ["Greataxe", "Javelin (4)", "Explorer's Pack"],
    "Bard": ["Rapier", "Diplomat's Pack", "Lute"],
    "Cleric": ["Mace", "Shield", "Chain Mail", "Holy Symbol"],
    "Druid": ["Scimitar", "Leather Armor", "Druidic Focus", "Explorer's Pack"],
    "Fighter": ["Chain Mail", "Longsword", "Shield", "Javelin (4)", "Explorer's Pack"],
    "Monk": ["Shortsword", "10 Darts", "Explorer's Pack"],
    "Paladin": ["Longsword", "Shield", "Chain Mail", "Holy Symbol"],
    "Ranger": ["Scale Mail", "Longbow", "20 Arrows", "Explorer's Pack"],
    "Rogue": ["Rapier", "Shortbow", "20 Arrows", "Burglar's Pack"],
    "Sorcerer": ["Dagger", "Component Pouch", "Arcane Focus"],
    "Warlock": ["Light Crossbow", "20 Bolts", "Component Pouch", "Scholar's Pack"],
    "Wizard": ["Quarterstaff", "Component Pouch", "Scholar's Pack"]
}

equipment = starting_equipment.get(random_class, [])

# Print character details
print("Race:", random_race)
print("Class:", random_class)
print("Gender:", random_gender)
print("Level:", random_lvl)
print(f"Strength: {ability_score_str} (Modifier: {str_modifier}, Bonus: {ability_score_str_bonus})")
print(f"Dexterity: {ability_score_dex} (Modifier: {dex_modifier}, Bonus: {ability_score_dex_bonus})")
print(f"Constitution: {ability_score_con} (Modifier: {con_modifier}, Bonus: {ability_score_con_bonus})")
print(f"Intelligence: {ability_score_int} (Modifier: {int_modifier}, Bonus: {ability_score_int_bonus})")
print(f"Wisdom: {ability_score_wis} (Modifier: {wis_modifier}, Bonus: {ability_score_wis_bonus})")
print(f"Charisma: {ability_score_cha} (Modifier: {cha_modifier}, Bonus: {ability_score_cha_bonus})")
print(f"Armor Class (AC): {ac}")
print(f"Hit Points (HP): {hp}")
print("Equipment:", ', '.join(equipment))
