# Iterable = list, tuple, string, set, dictionay this all are iterable.
# iterates = one by one that checks each items

# List
print("For List")
for item in ["one", "Two", "three", "Four"]:
    print(item)
# Tuple
print("For Tupple")
for item in ("one", "Two", "three", "Four"):
    print(item)
# Set
print("For Set")
for item in {"one", "Two", "three", "Four"}:
    print(item)
# String
print("For String")
for item in "1234":
    print(item)

# IMPORTANT - For dictionary there are 3 cases
# 1) printing only keys, 2) Printing only values, 3) Printing both key value
dict1 = {
   "1":"One",
   "2":"Two", 
   "3":"Three",
   "4":"Four"
}
print("To Print Both")
for item in dict1.items():
    print(item)

print("To Print Values")
for item in dict1.keys():
    print(item)

print("To Print Keys")
for item in dict1.values():
    print(item)
