# Tuple is nothing but immutable list. Its same as list just can't be modified
my_tuple = (1,2,"3")
print(my_tuple[1]) # This will give element at index 1
# my_tuple[1] = 3 # We can't do this in tuple
# Note - We can't sport or reverse the tuple
# We cam use "in" for tuple
print(1 in my_tuple)
# Tuple is faster than list

# Note we can do Tuple unpacking same as in list
x,y,z,*remain = (1,2,3,4,5,6,7,8,9)
print(x)
print(y)
print(z)
print(remain)

# Slicing can also be applied on tuplle
single = (1,2,3)
# Note - A tuple with single element will give comma at end
print(single[1:2])

# Note - Tuple has only 2 methods in total that is count and index
print(my_tuple.count(2)) # Returns number of 2 in that tuple
print(my_tuple.index("3")) #Returns the index of "3" if present else give error
print(len(my_tuple)) # Gives length of tuple
