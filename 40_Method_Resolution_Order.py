class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
for i in D.mro():
    print(i)
