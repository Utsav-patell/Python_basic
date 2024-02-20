# Don't Repeat Yourself
# say_hello() # Note - Always define your function before 
# Defining it
def say_hello():
    print("Hellooo")
say_hello()

# Arguments and Parameters
# Parameters are the variable which are passed at the time of define

def say_hello(name,emoji): # This are Parameters
    print(f"Hello {name} {emoji}")
# Positional Arguments - This is calling Method
say_hello("Utsav","💛") # This are Arguments

# Default Parameters - this is Defining Method
def say_hello(name="Harsh",emoji="💙"):
    print(f"Hello {name} {emoji}")

# Key Arguments - This is calling method
say_hello(emoji="🧡",name="Ayush") 

# Return Statement in Python
def sum(num1,num2):
    return num1 + num2
    print("I will not get executed")
print(sum(5,6))
# Note - As soon as 1st return statement comes python automatically breaks that function or its the last line.
# We can define another function inside a function.