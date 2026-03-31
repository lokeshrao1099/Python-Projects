import random


while True:
    print("Welcome to number guessing game created by Lokesh Yadav")
    print("Think a number between 1 and 100 and type it ")
    random_number = random.randint(1,100)
    attempt = 0
    
    guess_correctly = False
    play_again = False

    
    while guess_correctly == False:
        
        try:
            input_num = int(input("Enter your number here : "))
        except ValueError:
            print("Enter a number only")
        if random_number > input_num:
            print(f"Ohh sorry !You guess wrong. Enter a larger number than {input_num},Please Try again ")
            attempt= attempt+1
        elif random_number < input_num:
            print(f"Ohh sorry !You guess wrong. Enter a smaller number than {input_num},Please Try again ")
            attempt= attempt+1
        elif input_num > 100 or input_num < 1:
            print("Entered  number should be between 1 and 100")
        else :
            print("Congratulation ! You finally win the game.")
            print(f"You completed your game in {attempt} attempts")
            guess_correctly = True
    while play_again == False:
        again = input("Do you want to start a new game(Y/N) : ")
        if again == 'Y' or again == "y":
            play_again = True
            
        elif again == 'N' or again == 'n':
            exit()
            
        else:
            print("Please reply in Y/N stands for Yes/No")
    

            
   


    

