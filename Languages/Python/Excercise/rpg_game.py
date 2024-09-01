# OOP exercise 2
class Player():
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.max_health = 100
        self.weapon = weapon

    def __str__(self):
        player_weapon = self.weapon.name if self.weapon else "Empty"
        return f"Player {self.name} has {self.health}/{self.max_health} HP, Equipped {player_weapon}"
    
    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"Player {self.name} has equipped {self.weapon.name}!")
    
    def attack(self, target):
        weapon_dmg = self.weapon.get_damage() if self.weapon else 0
        total_dmg = max(weapon_dmg, 0)
        print(f"Player {self.name} deals {total_dmg} HP to {target.name}")
        target.take_damage(total_dmg)

    def take_damage(self, amount):
        self.health -= amount
        print(f"Player {self.name} took {amount} damage! Remaining Health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    def get_damage(self):
        return self.damage

new_weapon = Weapon("Void Sword", damage=13)
Player_1 = Player('Singular', 100, None)
Player_2 = Player('Singular2', 100, None)
Player_1.equip_weapon(new_weapon)
print(Player_1)
print(Player_2)
print("\n"*3)
Player_1.attack(Player_2)
