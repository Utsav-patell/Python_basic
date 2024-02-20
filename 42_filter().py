# Now Filter Function return the item values for which the function returns True and does not 
# return for which function return False

li = [1,2,3,4,5]
def only_odd(item):
    return item%2 != 0
print(list(filter(only_odd,li)))
#  All this return a new List.
