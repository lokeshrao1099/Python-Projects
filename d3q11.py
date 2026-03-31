def check(x):
  return int(x,2)%5 == 0

data = input().split(',')

x = list(filter(check,data))
print(",".join(x))