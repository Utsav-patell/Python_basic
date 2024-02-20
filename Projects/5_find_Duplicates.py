some_list = ["a","b","b","b","d","m","n","n"]
no_of_dup = 0 
duplicate_item = None
for item in some_list:
    no_of_dup = some_list.count(item)
    if duplicate_item == item:
        continue
    else:
        if no_of_dup >=2 :
            duplicate_item = item
            print(f"{item} has {no_of_dup} duplicates")
            no_of_dup = 0    
        else:
            no_of_dup = 0

# Better Solution
# duplicate = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicate:
#             duplicate.append(value)
#         else:
#             continue
    
# print(duplicate)    