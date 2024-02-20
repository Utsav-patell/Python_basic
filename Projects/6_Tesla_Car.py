def start_car(age):
    if age > 0:
        if age < 18:
            print("Sorry You are too Young. Powering OFF!")
        elif age == 18:
            print("Enjoy Your First Year of Driving. Powering ON!")
        else:
            print("Enjoy Your Ride. Powering ON!")
    else:
        print("Enter Valid Age")


age = int(input("Please Enter Your Age "))
start_car(age)
