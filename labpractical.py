
#Factorial
def fac(num):
    faci = 1
    if num >= 0 :
        for i in range(1,num+1): 
            faci = faci * i
        return faci
    else:
       return "Not Defined"
    

print(fac(int(input("enter your number : "))))

#palidrome or not
def palidrome(strng):
    if type(strng) == str:
        length = len(strng)
        string = strng.lower()
        is_pali = True
        for i in range(length // 2):
            if strng[i]!=strng[length-i-1]:
                print("The string is not palidrome")
                is_pali = False
                break
        if(is_pali== True):
            print("The string is palidrome")
    else:
        print("ERROR! Enter a string")

pal = input("Enter a string : ")
palidrome(pal)

#BMI CALCULATOR
def BMI_cal(weight,height):
    bmi = (weight/(height*height))
    print(bmi)
    if bmi<18:
        print("You are Underweight")
    elif 18 <= bmi< 25:
        print("You are Normal")
    elif 25 <= bmi < 35:
        print("You are Overweight")
    else:
        print("You are Obese")
weight = float(input("Enter your weight(in Kgs) : "))
height = float(input("Enter your height (in Mtr) : "))
BMI_cal(weight,height)
    
   
