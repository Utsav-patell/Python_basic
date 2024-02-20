from time import time
def performance(fn):
    def wrap(*args,**kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print(f"It tooks {t2 - t1} Seconds for {fn}")
        return result
    return wrap 
@performance
def fibo(num):
    print("FEBO Generator")
    n1 = 0
    n2 = 1
    iterator = iter(range(num-3))
    print(n1 , n2,end=" ")
    while True:
        try:
            sum = n1 + n2
            print(sum,end=" ")
            next(iterator)
            n1 = n2
            n2 = sum
        except StopIteration as e:
            print()
            break
        
@performance
def febo_normal(num):
    print("FEBO NORMAL")
    a = 0
    b = 1
    # print(a,b,end=" ")
    for i in range(num):
        sum = a + b
        print(sum,end=" ")
        a = b
        b = sum


fibo(1000)
febo_normal(1000)
