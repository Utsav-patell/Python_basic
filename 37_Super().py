class User:
    def __init__(self,email):
        self.email = email
        print(f"You are logged in with email - {self.email}")


class Archer(User):
    def __init__(self,name,attack, email):
        super().__init__(email)
        self.name = name
        self.attack = attack
    def power(self):
        print(f"My name is {self.name} & I have {self.attack} bows")

player1 = Archer("Arjun",50,"up188913@gmail.com")
player1.power()
