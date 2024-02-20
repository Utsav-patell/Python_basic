"""
== -> Compares the variable value AND variable-type. "1" != to 1
is -> Compares the memory location of the variable.
In Python [1,2,3] is not [1,2,3] because every data structure occupy 
different memory location. True for tupple, List, Dictionary, Sets
But "1" is "1" in python. True for boolean, String, Char, Int, Float
"""
# Double Equals
# print(1 == 1) # int = int and 1 = 1 
# print(True == 1) # int of true = 1 and 1 = 1
# print("1" == 1) # string != int
# print([1,] == 1) # list != int
# print((1,) == 1) # tuple != int
# print((1,) == [1,]) # list != tuple
print()
#  Is 
print(1 is 1)  # Same values of primitive data types occupy same memory location. 
print("1" is 1)
print("1" is "1")
print(True is True)
print((1,2,3) is (1,2,3)) # Exception - tuple with primitive type occupy same location
print((1,[1,2],3) is (1,[1,2],3))
print([1,2] is [1,2])


