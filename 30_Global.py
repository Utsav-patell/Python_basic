# Now suppose we want to access global varibale inside any function the for this we have 
# we have global keyword
# Example


balance = 0
# 1st Way using global keyword
def count(deposit):
    global balance
    balance +=deposit
    return balance
# print(count(1000))

# 2nd Way using global injection
def count1(deposit,balance):
    balance +=deposit
    return balance
balance = count1(1000,balance) # balance = 1000
balance = count1(1000,balance) # balance = 2000
balance = count1(1000,balance) # balance = 3000
# print(balance)
