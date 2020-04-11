import dndchar
import random

def createchar():

    #NAME
    playername = input("Enter character name: ")

    # RACE
    print("SELECT RACE")
    race = int(input("1. Human\n2. Dwarf\n3. Elf\n4. Gnome,\n5. Halfling\nChoice: "))
    races = [None, "Human", "Dwarf", 'Elf', 'Gnome', 'Halfling']
    playerrace = races[race]

    # CLASS
    print("\nSELECT CLASS")
    cls = int(input("1. Fighter\n2. Mage\n3. Cleric\n4. Rogue,\n5. Bard\nChoice: "))
    classes = [None, "Fighter", "Mage", 'Cleric', 'Rogue', 'Bard']
    playerclass = classes[cls]

    # ALIGNMENT
    print("\nSELECT ALIGNMENT")
    pick1 = int(input("1. Chaotic\n2. N/A\n3. Lawful\nChoice: "))
    pick2 = int(input("\n1. Evil\n2. Neutral\n3. Good\nChoice: "))
    p1 = [None, 'Chaotic', '', 'Lawful']
    p2 = [None, 'Evil', 'Neutral', 'Good']
    playeralignment = p1[pick1]+' '+p2[pick2]

    stats = [None, 'str', 'dex', 'int', 'wis', 'cha', 'con']
    rolls = [0,0,0,0,0,0]

    for i in range(6):
        currentrolls = []
        for j in range(4):
            currentrolls.append(random.randint(1,6))
        currentrolls.sort()
        currentrolls.pop(0)
        for val in currentrolls:
            rolls[i] += val
    rolls.sort(reverse = True)

    print(f"Your rolls: {rolls}")
    print(f"Possible stats: str, dex, int, wis, cha, con")
    for i in range(6):
        print(f"NOW ALLOCATING ROLL: {rolls[i]}")
        statchoice = input("Which stat would you like to apply this to? ")
        stats[stats.index(statchoice)] = rolls[i]

    # dndchar(name, race, class, alignment, str, dex, int, wis, cha, con)
    return dndchar.dndchar(playername, playerrace, playerclass, playeralignment,
                   stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], )

characters = []
for i in range(3):
    characters.append(createchar())
    characters[i].dowriting()
