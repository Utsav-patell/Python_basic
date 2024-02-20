# If we access an key of Dict that is not present then it will give an error. To Prevent this we 
# Have one methods that is get()
user = {
'name' :"Utsav",
"Gender" : "Male"
}
# print(user[age]) # IF we run program with this then it generate an error. Instead we can do

print(user.get("age",25))
# using Get it will generate new key with its value if the key is not present else 
# it will give the same value as in orignal list

user = {
'name' :"Utsav",
"Gender" : "Male",
 "age" : 21
}
print(user.get("age",25))
# Now this will not print 25 but it will print 21 bcz its already present

# 1) "in" Method - Used to search only key
print("name" in user)
print("name" in user.keys()) # used to know if key is present or not 
print("Utsav"in user.values()) # used to chec if the particular value is present or not
print(user.items()) #Gives tuple of key value pair of all the items (key & Value) in dict
#user.clear() # used to empty the dict
# print(user)
user2 = user.copy()
print(user2)

# 2) Pop
print(user2.pop("age")) # Returns the value of age and remove it
print(user2)

# 3) Pop item
print(user2.popitem()) # Removes the last key:value pair after python 3.7 update
# Earlier it removes randomly any key:value pair
print(user2) 

# 4) update() - used to add or update any keys value
user2.update({"name":"Ravi"})
user2.update({"age":"Utsav"})
print(user2)