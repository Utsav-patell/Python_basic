# This exp is used to make your code more short but at the tradeoff of readability
# Syntax - lamda funcname(para): one line exp
# Lets see how we can use lamda n prog 41, 42, 44
li = [1,2,3]

# Using Map
print(list(map(lambda item:item*2,li))) 
# Using filter 
print(list(filter(lambda item:item%2 != 0,li)))
# using reduce
from functools import reduce
accu = 0
print(reduce(lambda accu, item:accu+item,li))



# Excercise
print(list(map(lambda item:item**2,li)))

li2 = [(0,2),(4,3),(9,9),(10,-1)] # sort on the basis of 2nd number of tuple
li2.sort(key=lambda x:x[1])
print(li2)
