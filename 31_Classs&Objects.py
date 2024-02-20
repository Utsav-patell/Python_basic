# Now lets start the oops concept of Python. 1st is Class and Objects

# Suppose we have a player character as a class which create different players with name and their abilities

class PlayerCharacter:
    # Classs Object Attribute
    is_member = True # this is static variable if i change value using class name
    def __init__(self,player_name): # This is Constructor where self is similiar to this keyword.
        # Self is compulsory for every method of class except static method 
        self.player_name = player_name # This is varibale related to Object
    
    def sprint_run(self):  # This is method of class
        print("Running till 30 seconds")
    
P1 = PlayerCharacter("Spiderman") # Creating Object 
P2 = PlayerCharacter("Iron Man")

print(P1.player_name) 
print(P2.player_name)

P1.age = 22 # Defining age of Player 1.
print(P1.age) 
# print(P2.age)
P1.sprint_run()
P2.sprint_run()


print(P1.is_member)
print(P2.is_member)
print(PlayerCharacter.is_member)
# Now lets change value of is_member using class name
PlayerCharacter.is_member=False
print(P1.is_member)
print(P2.is_member)
print(PlayerCharacter.is_member)
# Note if i do P1.is_member = False then it create a new copy of is_memebr variable
 