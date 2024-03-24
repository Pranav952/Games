rock = '''
Rock choosed
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Papper Choosed
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors choosed
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

image = [rock, paper, scissors]
print("what do you chose?Type 0 for rock,1 for papper or 2 for scissor")
user_choice = int(input("Enter your choice"))
computer_choice = random.randint(0, 2)
if (user_choice == computer_choice):
    print(f"your choice {user_choice}:\n{image[user_choice]}")
    print(f"computer choice {computer_choice}:\n{image[computer_choice]}")
    print("Draw,Try again")
elif (user_choice > computer_choice):
    print(f"your choice {user_choice}:\n{image[user_choice]}")
    print(f"computer choice {computer_choice}:\n{image[computer_choice]}")
    print("You win")
elif (user_choice < computer_choice):
    print(f"your choice {user_choice}:\n{image[user_choice]}")
    print(f"computer choice {computer_choice}:\n{image[computer_choice]}")
    print("You lose")
else:
    print("Wrong choice,chose again")
