from functools import reduce

#1 Capitalize all of the pet names and print the list

def capitalize(li):
  return li.capitalize()

my_pets = ['sisi', 'bibi', 'titi', 'carla']

print(list(map(capitalize,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings , my_numbers[::-1])))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def only50(li):
  return li>50

print(list(filter(only50,scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def totals(l1,l2):
 # print(l1,l2)
  return l1 + l2

print(reduce(totals,(my_numbers + scores)))