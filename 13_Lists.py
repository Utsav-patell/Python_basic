# List = Odered sequence of Objects.
li1 = ["String", 1, True,"a",2.5]

# List can have only one data type or more then one data type mixed 
# It is a type of Data Structure (Organizing Data in a particular way)

amazon_cart = [
    "Notebook", 
    "Mobiles", 
    "Grapes",
    "Penicl",
    "Eraser",
    "Mango" 
]

print("Orignal",amazon_cart) # To print whole list
print(amazon_cart[0]) # Print Particular object

# print(amazon_cart[5]) # This will give an index Error if bcz only total 0-3 index is there.

# List Slicing
print(amazon_cart[2::2]) # apply Same concept as string
# Note - String was immutable but List is muttable so we can change oject by index number
amazon_cart[2] = "Cover"
print(amazon_cart)

# Note - List slicing creates a whole new copy of List. See below example
# Using slicing
new_cart = amazon_cart[::]
new_cart[1] = "Television"

print("new_cart -",new_cart)
print("amazon_cart -",amazon_cart)

# Without using Slicing
new_cart = amazon_cart
new_cart[1] = "Television"
# The change of Television will occur in both the list
print("new_cart -",new_cart)
print("amazon_cart -",amazon_cart)

# Reason - Direct assingment gives the address of amazon_cart to new_cart while in slicing 
# It gives the copy of the list


