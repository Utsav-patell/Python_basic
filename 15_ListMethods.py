# Adding Methods

# 1) Append
list_1 = [0,1,2,3,4,5,6]
new_list = list_1.append("New") # Add the object to the last position of List
print (list_1)
print(new_list)

# Note Appdend does not return anything means it does not create any new list  
# That is why new_list remained empty

# 2) Insert
list_1 = [0,1,2,3,4,5,6]
new_list = list_1.insert(3,"New") # Add the object at particular index 
# and shift elements to right Syntax - insert(index,Object)
print (list_1)
print(new_list)

# Note Insert does not return anything means it does not create any new list  
# That is why new_list remained empty

# 3) Extend
list_1 = [0,1,2,3,4,5,6]
new_list = list_1.extend(["new1","new2","new3"]) # Add multiple list of objct at last of list
print (list_1)
print(new_list)

# Note Extend does not return anything means it does not create any new list  
# That is why new_list remained empty

# Removing Methods
# 1) Pop(index) 
list_1 = [0,1,2,3,4,5,6]
new_list = list_1.pop() # remove last objct of list
print (list_1)
print(new_list)
# pop returns the element that is removed if we take it in any other variable
new_list = list_1.pop(2) # remove objct of index 2 of list
print (list_1)
print(new_list)

# 2) Remove(value/elemnet)
new_list = list_1.remove(1) # remove element with value "2"
print (list_1)
print(new_list)
# it returns nothing so new list is none
# If we try to remove the value that is not present in the list then it gives an "value error"
# new_list = list_1.remove(1)   

# 2) clear()
new_list = list_1.clear() # clear the whole list
print (list_1)
print(new_list)
# it returns nothing so new list is none

# Searching Methods
# 1) index(element)
basket = ['a','b','c','d','e']
print(basket.index("d"))
# This will give index at which the element is present
# If the list does not contains it then index() will generate an error
# For this we can use "in" keyword which returns true or false based on the element is presence
print("a" in basket)

# 2) Count - Counts the number of times particular element is present

basket = ['a','b','c','d','e','c',1,"1"]
print(basket.count("c"))

# Sorting Methods and Function
# 1) sort method
list2 = ["x", "y","a","b","c","f"]
new_list2 = list2.sort() # This will change the list 2 itself and does not produce any new list
print(list2)  
print(new_list2) # So new_list2 is none

# 2) Sorted Function

list2 = ["x", "y","a","b","c","f"]
new_list2 = sorted(list2) # Sorted is same as sort but it does not change the main list. It 
# produces a new list an that is why new_list2 is sorted form of list2
print(list2)  
print(new_list2)

# 3) Reverse
list2 = ["x", "y","a","b","c","f"]
new_list2 = list2.reverse() # This reverses the whole list
print(list2)  
print(new_list2)

# Shortcuts 
# 1) Range 
print(list(range(0,100))) # This will help us to create big list
# Shortcuts - range(start,stop)

# 2) join
sentence = "+"
new_sentence = sentence.join(["Hi","my","name","is","Utsav"])
print(sentence)
print(new_sentence)



