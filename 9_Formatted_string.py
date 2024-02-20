# Formated Strings
# Suppose we want a dynamic string for an amazon page then a normal and 
#  non-professional way is

name = "Utsav"
age = 25
print("Hi "+ name + ".Your age is "+ str(age) )

# Another way . Available only in Python 3 (preffered)
print(f"Hi {name}. Your age is {age}")

# Old way of formated strig which is available in python 3 and 2 both is 
print("Hi {}. Your age is {}".format(name,age))
print("Hi {1}. Your age is {0}".format(name,age)) # We can even change the variable posi by index number
print("Hi {new_name}. Your age is {age}".format(new_name='Vatsal',age = 25)) # We need to apply var name



