# Break - It will break out of the loop and will exit and never iterate the loop again.
for item in range(1,6):
    if item == 4:
        break
    print(f"If item is not 2 and it is {item}") # 1, 2 ,3
# Continue - It will break out of loop for that particular iteration not for whole.
print("\ncontinue\n")
for item in range(1,6):
    if item == 4:
        continue
    print(f"If item is not 2 and it is {item}") # 1, 2 ,3,5
# Pass - It is used only for debugging purpose and rarely in real code

for item in range(1,6):
    # Still thinking the content
    pass #Comment this pass and you will get indentation error