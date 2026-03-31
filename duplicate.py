# exercise to check deplicate values
some_list = ["a","b","c","d","e","e","d"]

duplicate = []

for char in some_list:
  if some_list.count(char) > 1:
    if char not in duplicate:  # to not repeat char in duplicate list
      duplicate.append(char)

print(duplicate)
  
    
    
    
    
