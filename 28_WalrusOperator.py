#  := is the walrus operator which is used to assign a value to variable 
#  use that expression in a condition at same time. See example for reference

word = "Hellooooooo"
if((n:=len(word))>5):
    print(f"word is too long of letter {n}")
# This is usefull when we have a very big expression.

