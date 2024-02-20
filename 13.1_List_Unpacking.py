a,b,c = [1,2,3]
print(a)    
print(b)
print(c)

a,c,*remains,d,e  = [1,2,3,4,5,6,7,8,9]
print(a)    
print(c)
print(remains)
print(d)
print(e)

# in this way we can unpack list into a individual variable. By wrtiting *var_name we can 
# assign all the elements to that variable. Note only one such varibale is allow 
# means we can't write a,b,c,*remain1,d,*remain2 
