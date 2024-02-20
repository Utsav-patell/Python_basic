# There are two type of indexing in python that is Positive and negative

# Positive Index  
selfish = "012345678" # Index = 012345678
print(selfish[0:8:1])  # Syntax str_name[start:end:stepover]
# Note - The end point is not included so to print whole string we write
# Start = 0 and End = str_length stepover - MEans by how much to increament
# Important Cases
print("[0::] " + selfish[0::]) # Default value of end = Full string
print("[:5:] " + selfish[:5:]) # Default value of start = 0
print("[::] " + selfish[::])  # default value of Stepover = 1
# Size = End - Start

# Negative Index
Negative = "012345678"
print("[-1] " + Negative[-1])
print("[-1:-10:-1] "+Negative[-1:-10:-1]) # A reverse string is printed using negative indexing
print("[-1::-1] "+Negative[-1::-1]) 
print("[::-1] "+Negative[::-1])

# To print normal string using negative index we have to do as below
print("[-10:-1:1] "+Negative[-10:-1:1])  
# We can never print the last alpha of the string using negative indexing at end 
print("[-10:10:1] " + Negative [-10:10:1])
# We can do this by using last number index at end

# Strings are Immutable means we can overwrite but can't edit the string by indexes
# Eg - we can't do str[2] = 'a'

# selfish[0] = '2' We will get the error in this
# print(selfish)