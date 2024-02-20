# Escape Sequence - It consider the thing after \ as string even if its a special character 
#  Suppose i want to write in string as below 
# It's a "sunny" weather today.  If i try normally then lets see we what happens. (Remove comments)
# Weather = "It's a "sunny" weather today"
# print(Weather)

# After using escape sequence
Weather = "It\'s a \"sunny\" weather today"
print(Weather) 

#  There are some imp escape seq for output formating. 
"""
\n = New_line
\t = Tab space
\\ = to print \
\\n = to print \n 


"""