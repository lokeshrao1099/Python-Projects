#code to print duplicate value using comprehension 

some_list = ['a','b','c','b','d','n','n','m']

my_list = list({dup for dup in some_list if some_list.count(dup) > 1  })

print(my_list)