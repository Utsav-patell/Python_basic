my_sets = {1,2,3,4,5,5}
# Sets is same as normal set in Maths. So it does not support repeatation 
print(my_sets)
# We can add new element in sets using "add" method
my_sets.add("Hi")
print(my_sets)
# Note we can add already present element in set
my_sets.add(1)
print(my_sets)
new_set = my_sets
print(new_set)
new_set.add(12)
print(my_sets) # Note changes in new_set is apllied in old set bcz every thing is object in python
# To create a copy we can use copy method instead
new_set = my_sets.copy()
new_set.add(7)
print(new_set)
print(my_sets)
