class Archer:
    def attack(self):
        print("Archer is attacking")
class Wizard:
    def attack(self):
        print("Wizard is attacking")
P1 = Archer()
P2 = Wizard()
for player in [P1,P2]:
    player.attack()
# Polymorphism means one thing many form. Here method Attack is giving different output
# based on the object by which it is called.