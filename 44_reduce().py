from functools import reduce
li = [1,2,3,4,5]
def accumulator(acc,item): # First - initial Value of acc and Second = First value of iterable
    print(f"acc = {acc},item = {item}")
    return item + acc
print(reduce(accumulator,li,0))  # reduce (function,iterable,starting of acc)
