# Map() Function is the most used function in python. 
""" Map() function returns a map object(which is an iterator) of 
the results after applying the given function
to each item of a given iterable (list, tuple etc.)"""
# It automatically iterate the iterable
li = [1,2,3,4]
def multiply_by2(item):
    return 2*item
print(list(map(multiply_by2,li)))
# Note - map function returns object of iterable so we have to again convert to List,tuple 
# anything

# Syntax - map("action",iterable)
