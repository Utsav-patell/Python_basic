class MyPlayer :
    __name = ""
    _age = None
    def set_name(self,name,age):
        self.__name = name
        self._age = age
    def disp(self):
        print(f"My name is {self.__name} and I am {self._age} year old")
Player1 = MyPlayer()
Player1.set_name("Utsav",15)
Player1.disp()
Player1.__name = "Ravi"
Player1.disp()

""" Note-: prefix __name means Private and prefix _name means Protected. But its just 
 a convention and there is nothing like private and protected in python.
"""
 
