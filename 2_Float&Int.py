# Fundamental data types

# 1) Integers
print(type(2+4))
print(type(2-4))
print(type(2*4))
print(type(2%4)) # Returns reminder of 2/4 % = modulo operator 
# 2) Float
print(type(2/4))
print(type(1.1 + 9.9))
"""We need more memory to store floating point number because in memory area, 0.5 is stored 
at 2 different places 1 for 0 and 1 for 5. So it required more space then 
int due to decimal point.""" 

#  Mic Operator
print(type(2**4)) # Ans - 16  2 to the power 4
print(type(5//4)) # Ans - 1 It does normal division but it return int type instead of float as shown above.

# Maths Function
print(round(4.967,2)) # Round off the number
print(abs(-29)) # Print only the absolute number mean positve

# Complex() function and Bin() function
# Complex numbers are rarely used that are (Real number + 1j*Number)
print(complex (5+2*1j))

# bin() stand for binary number and it is used ti convert any integer or float into binary.
print (bin(5)) 
# Note - We can convert binary into normal int by using below thing

print(int('1011',2))