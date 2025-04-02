import random

rock = '''
    -----
---' ____)
      (____)
      (____)
      (____)
---.__(___)
'''

paper = '''
    -------
---'    ___)_____
           ______)
           _______)
        _________)
---.___________)
'''

scissors = '''
    ------
---'   ___)_____
          ______)
          _______)
      (____)
---._(____)
'''

keys = [rock, paper, scissors]
user_choice = int(input("What is your choice? 0 - Rock, 1 - Paper, 2 - Scissors. \n"))
print("User's choice:")
if user_choice >= 0 and user_choice <=2:
    print(keys[user_choice])

computer_choice = random.randint(0, 2)
print("Computer's choice:")
print(keys[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("This is an invalid option. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print('You win!')
elif computer_choice == 0 and user_choice == 2:
    print('You lose!')
elif computer_choice > user_choice:
    print('You lose!')
elif user_choice > computer_choice:
    print('You win!')
elif computer_choice == user_choice:
    print("It's a draw!")