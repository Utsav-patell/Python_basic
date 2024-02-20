#  Lets Make a program that takes age from the user and display it

# while True:
#     try:
#         age = int(input("Enter your Age "))
#         c = 10/age
#         print(f"Your age is {age}")
#     except ValueError:
#         print("Please Enter Valid Number")
#     except ZeroDivisionError:
#         print("Please enter number Greator then 0")
#     else:
#         print("Thank You")
#         break


    # Some importants ways to handle error

# def sum(num1 , num2):
#         try:
#             num1/num2
#             return num1 + num2
        
#         except (TypeError,ZeroDivisionError) as err:
#             print(f"The error occured is {err}")
#         finally:
#              print("The block has finally ended")
# print(sum(1,'2'))

    # Forcefully raising the error

def sum(num1 , num2):
        try:
            num1/num2
            num1 = num1 + num2
            raise Exception("Enter Number greator then 10")
        except (TypeError,ZeroDivisionError) as err:
            print(f"The error occured is {err}")
        finally:
             print("The block has finally ended")
print(sum(1,3))
