#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
letter = 0
symbol = 0
number = 0
total_cr = nr_letters + nr_numbers + nr_symbols
for turn in range (0, total_cr):
  random_cr = int(random.randint(1,3))
  if random_cr == 1:
    if letter <= nr_letters:
      letter += 1
      random_lt = int(random.randint(0,51))
      password.append(str(letters[random_lt]))
  elif random_cr == 2:
    if symbol <= nr_symbols:
      symbol += 1
      random_sym = int(random.randint(0,8))
      password.append(str(symbols[random_sym]))
  elif random_cr == 3:
    if number <= nr_numbers:
      number += 1
      random_num = int(random.randint(0,9))
      password.append(str(numbers[random_num]))

password_final = ""
for char in range (0, total_cr - 1):
  password_final += password[char]
print(password_final)
    