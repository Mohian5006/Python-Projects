# Even or Odd Counter
print("Welcome to Even or Odd Counter!")

list_even_odd = []
even_count = []
odd_count = []
even = 0
odd = 0

digits = int(input("How many digits do you want in a list? \n"))

# Taking user input as list
for i in range(digits):
    number = int(input(f"Enter number {i+1}: \n"))
    list_even_odd.append(number)
print("List that you've entered:")
print(list_even_odd)

# Checking even or odd

for e in list_even_odd:
    if e%2 == 0:
        even_count.append(e)
    else:
        odd_count.append(e)

# Counting how many numbers are even and how many are odd
even = len(even_count)
odd = len(odd_count)

# Printing the count of even and odd numbers
print(f"Even count: {even}")
print(f"Odd count: {odd}")

    