def tesla():
  user_age = int(input("Enter your age : "))
  if user_age < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif user_age == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")
  elif user_age >18:
    print("Power on. Enjoy your ride")

tesla()
  