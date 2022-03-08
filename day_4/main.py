import random


# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}")

# random_side = random.randint(0,1)
# if random_side == 1:
#   print("heads")
# else:
#   print('tails')

# states_of_america = ["Delaware", "Pennsylvania"]

# print(states_of_america[0])

# states_of_america[1] = "Pencilvania"

# states_of_america.append("Angelaland")

# print(states_of_america)

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# # x = len(names)
# # random_choice = random.randint(0, x - 1)
# # person_paying = names[random_choice]
# person_paying = random.choice(names)
# print(person_paying + " is going to pay for the meal")

# dirty_dozen = ["straberries", "spinach", "kale", "nectarines", "appples", "grapes", "peaches", "cherries"]

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3] 
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# horizontal = int(position[0] ) - 1
# vertical = int(position[1] ) - 1

# selected_row = map[vertical]
# selected_row[horizontal] = "x"




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
  print("Invalid number!")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0,2)
  print(f"Computer chose:")
  print(game_images[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("User wins!")
  elif user_choice >= 3 or user_choice <0:
    print("That is invalid")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif user_choice > computer_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("Computer wins!")
  elif computer_choice == user_choice:
    print("It's a draw")