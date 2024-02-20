Dictionary = {
    "key1": 1, # Integer
    "key2": "2", # String
        3: 3, # Key is Integer
        True:False # Bollean
}
print(Dictionary)
print(Dictionary[3])
print(Dictionary[True])
# Note - Dictionary is not at adjacent memory location they are like linked List. Scattered 
# All accros the memory.
# If we print big dictionary then it is not neccesary that they are printed in same order
# Dictionary is a type of Data Structure so it can have more then one data-type for same list

# We can also have a dictionary inside List 
Mixed = [
{
    "key1": 1, # Integer
    "key2": "2", # String
    3: 3, # Key is Integer
    True:False # Bollean
},
{
    "key1.1": 1, # Integer
    "key2.2": "2", # String
    3.3: 3, # Key is Integer
    True:False # Bollean
}
]
print(Mixed[1]["key1.1"])

# As a key in Dictionary we can use only those data types that are immutable 
# eg - string, Integer, Float , Tupple, Boolean etc

# Creating Dictionary With Dict keyord 
user = dict(name="Utsav") # A dictionary is created of name user
print(user)
print(user["name"])
