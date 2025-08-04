# Guessing the number
import random

print("Welcome to Guess the Number game!!!\n")

# Generating the random number from 1 to 20
number = random.randint(1,20)

print("You have 5 guess only.")

for i in range(6):
    user_input = int(input(f"Enter your guess {i+1}: "))

    # Guessinng the number
    if user_input == number:
        print(f"You guessed it right and the number is : {number}")
        break
    elif user_input > number:  
        print("Too High!")
    else:
        print("Too Low!")
        