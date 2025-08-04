import random

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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

rock_paper_scissor = [rock, paper, scissor]

print("Welcome to Rock-Paper-Scissor game! ")
user_input = int(input("First, it is your turn. Type 0 for Rock, 1 for Paper or 2 for Scissor. "))

if user_input > 2:
    print("Invalid Number.")
else:
    print(f"You chose: {rock_paper_scissor [user_input]}")

    computer = random.randint(0,2)

    print(f"Computer chose: {rock_paper_scissor [computer]}")

    if user_input == computer:
        print("It's a Draw!!!")

    elif user_input == 0 and computer == 1:
        print("You Lose!!!")
    elif user_input == 0 and computer == 2:
        print("You Won!!!")
    elif user_input == 1 and computer == 0:
        print("You Won!!!")
    elif user_input == 1 and computer == 2:
        print("You Lose!!!")
    elif user_input == 2 and computer == 0:
        print("You Lose!!!")
    elif user_input == 2 and computer == 1:
        print("You Won!!!")
