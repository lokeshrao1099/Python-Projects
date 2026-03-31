x,y = map(int,input().split(','))
lst = []

for i in range(0,x):
  tmp = []
  for j in range(0,y):
    
    tmp.append(i*j)
  lst.append(tmp)

print(lst)