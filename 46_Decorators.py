# In Python Function are the first class citizen which act as normal variable only.
# def func():
#     print("Helllo")
# var = func()
# del func
# var
# Here var has taken the defination of func so even if we delete the func only the address of the name 
# func is delete but the defination is still there.
# Note the function which accepts function as parameter or return function then it is higher order functions.

#  A Decorator is nthing but but another function that wraps another function and enhances it, changes it or modify the orignal function.

def my_decorator(func):
    def wrap_func():
        print("*****")
        func()
        print("*****")
    return wrap_func
# Now suppose if i want to add aditional functionality to func function then I just have to change my decorators wrapper funcion.
@my_decorator
def Hello():
    print("HElllllo") 

Hello()
# The Decorator Pattern 
def decorator_pattern(func):   # This pattern is know as decorator pattern
    def wrap(*args,**kwargs): # This pattern is know as decorator pattern
        func(*args,**kwargs) # This pattern is know as decorator pattern
    return wrap # This pattern is know as decorator pattern

@decorator_pattern
def greet(greet,name="Utsav"):
    print(greet,name)

greet("Hello")

#  Application of Decorators
# 1) Static and Class Methods
# 2) To calculate The time
# 3) Login request for a services.

