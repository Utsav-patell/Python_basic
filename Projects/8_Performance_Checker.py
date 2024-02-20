from time import time
def performance(fn):
    def wrap(*args,**kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print(f"It tooks {t2 - t1} Seconds")
        return result
    return wrap 

@performance
def tempFunc():
    for i in range(1000009000):
        i = i+ 1
    
tempFunc()