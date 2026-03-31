def OddEven(num):
    if num%2==0:
        print("The number {} is even".format(num))
    else:
        print(f"The number {num} is Odd")
    
num = int(input("The a number : "))
OddEven(num)
