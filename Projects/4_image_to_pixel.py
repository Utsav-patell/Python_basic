picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,1,1,1,1,1,0],
    [0,0,1,1,1,0,0]
]

# Now Lets convert this picture such that 0 = no pixel and 1 = pixel denoted by "*"

for image in picture:
    for pixel in image:
        if(pixel == 0):
            print(" ",end = "")
        else :
            print("*",end = "")
    print()