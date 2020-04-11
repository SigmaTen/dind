import random

class dndchar:

    def __init__(self, name, race, cls, alignment, str, dex, int, wis, cha, con): # <---- CONSTRUCTOR
        self.name = name
        self.race = race
        self.cls = cls
        self.alignment = alignment
        self.stats = {'str':str, 'dex': dex, 'int':int, 'wis':wis, 'cha':cha, 'con':con}

    def dowriting(self):
        print(f"Name: {self.name}")
        for stat in self.stats.items():
            print(f"{stat}")

    def givestats(self, stats = [], amts = []):
        for stat in stats:
            self.stats[stat] += amts[stats.index(stat)]
            if self.stats[stat] > 30:
                self.stats[stat] = 30
            elif self.stats[stat] < 1:
                self.stats[stat] = 1

    def calcbonus(self, stat):
        modifiers = [None, -5, -4, -4, -3, -3, -2, -2, -1,
                    -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
                     6, 6, 7, 7, 8, 8, 9, 9, 10]

        return modifiers[self.stats[stat]]

    def roll(self, dice = [], stattype = []):
        rolls = []
        for die in dice:
            rolls.append(random.randint(1,(die)) + self.calcbonus(stattype[dice.index(die)]))

        return rolls


# TEST CODE
if __name__ == '__main__':
    christoph = dndchar('Kevin',10,7,13,12,1,10)
    christoph.dowriting()
    christoph.givestats(['str'], [50])
