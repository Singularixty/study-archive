class Item:
    def __init__(self, name, damage, durability):
        self.name = name
        self.DMG = damage
        self.DURABILITY = durability

default_fist = Item("Fist", 1, 9999999)

class Player:
    def __init__(self, name, item=None):
        self.name = name
        self.HP = 100
        self.DEF = 1
        self.ITEM = item if item else default_fist

    def TakeItem(self, item):
        self.ITEM = item

    def Attack(self, target):
        if self.ITEM.DURABILITY > 0:
            damage_dealt = self.ITEM.DMG
            target.TakeDamage(self.name, damage_dealt)
            self.ITEM.DURABILITY -= 1
            print(f"{self.name} attacked {target.name} for {damage_dealt} DMG!")
        else:
            print(f"{self.name} tried to attack, but the item is broken!")

    def TakeDamage(self, monster_name, damage):
        total_damage = damage - self.DEF
        self.HP -= total_damage
        print(f"{monster_name} attacked {self.name} for {total_damage} DMG! Remaining HP: {self.HP}")

Dragon_Sword = Item("Dragon Sword", 10, 200)
Player_1 = Player("Sigular")
Player_2 = Player("Sigular2", Dragon_Sword)

Player_2.Attack(Player_1)
Player_2.Attack(Player_1)
Player_2.Attack(Player_1)