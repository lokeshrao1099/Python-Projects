#List Comprehension
my_list = [num**2 for num in range(0,101) if num % 2 == 0]

print(my_list)

#Set Comprehention
my_list = {num**2 for num in range(0,101) if num % 2 == 0}

print(my_list)

#Dictionary Comprehension 

simple_dict = {'a':1,'b':2}

my_dict = {k:v**2 for k,v in simple_dict.items() if v % 2 == 0}

print(my_dict)