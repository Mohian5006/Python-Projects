#Password generator
import random
letters = ['a','b','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator made by Mohian!")

nr_letters = int(input("How many letters would you like in your password???\n"))
nr_symbols = int(input("How many symbols would you like in your password???\n"))
nr_numbers = int(input("How many numbers would you like in your password???\n"))


# Creating empty list to store the randomly picked letters, symbols and numbers
password_list = []

# Listing Letters
for picked_letter in range(0, nr_letters):

    #password_list += random.choice(letters) --- This login also works. Both random.append and += logic works in same way

    password_list.append(random.choice(letters)) # Adding item to the end of the list

# Listing Symbols
for picked_symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols)) # Adding item to the end of the list

# Listing Numbers
for picked_number in range(0, nr_numbers):
   password_list.append(random.choice(numbers)) # Adding item to the end of the list

# Randize the items in the list
random.shuffle(password_list)

# # Join the items in the list into a string
# password =''.join(password_list)


# Randomizing the password using For Loop
final_password = ""

for char in password_list:
    final_password += char


print(f"Your generated password is: {final_password}")
