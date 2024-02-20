class user():
    def is_verified(self):
        return True
class Archer(user): # Here we inherited user user inside Archer
    def Attack(self):
        if(self.is_verified()):
            print("You Can shoot Arrows")
p1 = Archer()
p1.Attack()
p2 = user()

# Now during debugging a function which is used to check if a instance is a part of a 
# partcular class or not then we uses isinstances(object_name, Class_name) function

print(isinstance(p1,user))
print(isinstance(p1,Archer))
print(isinstance(p2,Archer))

