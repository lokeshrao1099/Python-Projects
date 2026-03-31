lst = []
while True:
  x = input()
  if len(x) == 0:
    break
  lst.append(x.upper())

for i in lst:
  print(i)

