class Player():
    def __init__(self, Name, Score):
        self.Name = Name
        self.Health = 100
        self.Score = Score

    def DamagePlayer(self, damage):
        self.Health -= damage

Player1 = Player('Thomas', 0)
print(Player1.Health)
Player1.DamagePlayer(15)
print(Player1.Health)
