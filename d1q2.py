#my solution
def fac(num):
  faci = 1
  for i in range(1,num+1): 
    faci = faci * i
  return faci

print(fac(int(input("enter your number"))))


# reduce tool
from functools import reduce

def fun(acc, item):
	return acc*item

num = int(input())
print(reduce(fun,range(1, num+1), 1))

#while and try
while True:
try:
    num = int(input("Enter a number: "))
    break
except ValueError as err:
    print(err)

org = num
fact = 1
while num:
    fact = num * fact
    num = num - 1
print(f'the factorial of {org} is {fact}')
    