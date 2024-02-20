# we can make our own data type which have power of other data types by extending that class.
class SuperList(list):
    def __len__(self):
        return 100
S1 = SuperList()
S1.append(5)
print(S1[0])
print(len(S1))


    