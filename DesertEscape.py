import random
print("""Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The bandits want their camel back and are chasing you down! Survive your
desert trek and out run the bandits.""")
# Question 1: Variable Starting Values
done = False
miles = 0
thirst = 0
tired = 0
bandits = -20
drinks = 3

while not done:
  print("""
          A. Drink from your canteen.
          B. Ahead moderate speed.
          C. Ahead full speed.
          D. Stop for the night.
          E. Status check.
          Q. Quit.""")
  choice = input("Your choice? ").upper()#.upper() makes it so the player can use capital or lower case letter.
    
  #Question 2: Different Choices
  if choice == 'A':
    if drinks >= 1:
      drinks = drinks - 1
      print("Your thirst has been quenched")
    else:
      print("You have no water left!")
  elif choice == 'B':
    miles = miles + random.randint(5, 12)
    print("You traveled", miles, "miles")
    thirst = thirst + 1
    tired = tired + 1
    bandits = bandits + random.randint(7, 14)
  elif choice == 'C':
    miles = miles + random.randint(10, 20)
    print("You traveled", miles, "miles")
    thirst = thirst + 1
    tired = tired + random.randint(1, 3)
    bandits = bandits + random.randint(7, 14)
  elif choice == 'D':
    tired = 0
    bandits = bandits + random.randint(7, 14)
    print("The camel is happy!")
  elif choice == 'E':
    print("Miles Traveled: ",miles,
          "\nDrinks In Canteen: ",drinks,
          "\nThe bandits are", miles - bandits, "miles behind you!")
  elif choice == 'Q':
    done = True
    print("You've quit now no one knows what'll happen to you...")
    
    
      

  #Question 3: Canteen Check and Camel Check
  
  if thirst >= 6:
    print("You died of thirst!")
    done = True
  elif thirst >= 4 and not done:
    print("You are thristy")

  if tired >= 8 and not done:
    print("Your camel died of thirst!")
    done = True
  elif tired >= 5 and not done:
    print("Your camel Is getting tired.")
  
#Question 4: Bandit Check and Escape Desert Check
  if miles - bandits <= 0 and not done:
    done = True
    print("The bandits caught you! GAME OVER ")
  elif miles - bandits <= 15 and not done:
    print("The bandits are catching up!")
  if miles >= 200:
    done = True
    print("You've crossed the desert, congratulations you won!")
  #Honors Question 5: Oasis