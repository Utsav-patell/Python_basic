# Range is an inbuilt function which returns object that represent sequence of object
#   iterates from start to end point with given step over

print(list(range(0,10))) # A list from 0 to 10 (10 not included)
print(tuple(range(10))) # A tuple from 0 to 10 (10 not included)
print(range(10)) # An object range(0, 10)

# Range is usually used with loops in python
# syntax - range(start, stop, step) 
for number in range(0,10,1): # Iterates from 0 to 9 with step of 1
    print(number) 

# Enumartes is a function which iterates the index-value pair of interable.
for index in enumerate("Helllo"):
    print(index)

for index,value in enumerate("Helllo"):
    print(f"index of {value} is {index}")
print(list(enumerate("Hellllo"))) # Creates tuple of list
print(tuple(enumerate("Hellllo"))) # Creates tuple of tuple
print(dict(enumerate("Hellllo"))) # Creates Dictionary