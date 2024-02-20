# Application Of *args and **kwargs
def total(*args,**kwargs):
    # print(**kwargs)
    add = 0
    for i in kwargs.values():
        add = add + i
    print(sum(args)+add)
# total(1,2,3,4,5,6,7,10,num1=5,num2=30)
# Note args create tuple if we print it with * else it gives number one by one
# While Kwargs give key value pair that is dictionary . So to use its value we need to use its methods
def disp(*args,**kwargs):
    print(*args)
    print(args)
    print(kwargs)
disp(1,23,4,5,6,7,n1= 20,n2= 30)

#  Rule to make such function
# funct("Normal Parameters","*args","default parameter","**kwargs")
# Note we can give custom name instead of args nd kwargs.
