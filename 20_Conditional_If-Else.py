# Conditional statements are used to control the flow of program acc to the logic
is_old = True
is_licenced = True
# Be Care-Ful of indentaation
if is_old :
    print("Inside If")
elif is_licenced :
    print("Inside elif")
else :
    print("Inside Else")
print("Outside If-else")

# Tuthy vs Falsey Values
"""
all values are considered "truthy" except for the following, which are "falsy":
- None
- False
Numbers that are numerically equal to zero, including:
- 0
- 0.0
- 0j
- decimal.Decimal(0)
- fraction.Fraction(0, 1)
Empty sequences and collections, including:
- [] - an empty list
- {} - an empty dict
- () - an empty tuple
- set() - an empty set
- '' - an empty str
- b'' - an empty bytes
- bytearray(b'') - an empty bytearray
- memoryview(b'') - an empty memoryview
- an empty range, like range(0)
- objects for which
- obj.__bool__() returns False
- obj.__len__() returns 0, given that obj.__bool__ is undefined 
"""

# Ternary Operation - It is also called conditional expressions. Syntax is as below
# "StatementForTrue" if condition else "statementForFalse"
age = 15
driving = "Allowed" if age>=18 else "Not Allowed" 
print(driving)
# This is an shorthand notation of If-Else


