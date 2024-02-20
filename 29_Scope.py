# 
a = "In Global scope of Program"

def confusion():
    # a = "Inside Local scope of Confusion"
    return a
def parentConf():
    a = "inside Parent scope of Confusion"
    return confusion()
    # return sum # Comment upper line to understand 4th rule
    
print("a = ",a)
print("confusion() - ",confusion())
print("parentConf() - ",parentConf())
# Remove or add "a" variable to see different outputs

# Predict the Output
#  Note Python different variable if the given variable with same name is in Function

#  Rules of the scope in Python
# 1) Check if the variable is in local scope. If yes then change it only else
# 2) Check if the variable is in Parent scope. if yes Then change it else 
# 3) Check If the variable is in Global Scope. If yes then change it else
# 4) Check if the variable is an Inbuilt function. If yes then print it.

# See below Example

