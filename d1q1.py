#my method
def div7(first,last):
  list = []
  for i in range(first,last+1):
    if i % 7 == 0 and i % 5 !=0 :
      list.append(i)
  return list

print(div7(2000,3200))

#using generator
print(*(i for i in range(2000,3201) if i % 7 == 0 and i % 5 != 0),sep=",")