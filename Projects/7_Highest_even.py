def highest_even(li):
    li.sort()
    for value in li[::-1]:
        if(value%2==0):
            print(value, "is the highest even")
            break
        else:
            print("No even number found")
highest_even([100,-100,23,4,5,22,0])
