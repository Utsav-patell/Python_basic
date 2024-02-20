# Dunder name is just short form of double underscore method made by programers.
# For some purpose this methods are overriden for particular Instances.
class Demo():
    def __init__(self):
        print("This is INIT method")
    def __str__ (self):
        print(f"Str is called")

class Demo1():
    def __init__(self):
        print("This is INIT method")
d1 = Demo()
d1.__str__()
d2 = Demo1()
print(f"without overriding dunder method {d2.__str__()}")