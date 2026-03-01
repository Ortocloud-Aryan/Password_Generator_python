letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '?', '/']

letters_no = int(input("how many letters of the alphabets would you like to have?\n"))
numbers_no = int(input("how many Numbers do you want?\n"))
symbols_no = int(input("how many symbols do you want?\n"))
#passwrod generator :
import random

password_list = []

for l_no in range(0, letters_no):
  random_letter = random.choice(letters)
  password_list.append(random_letter)

for n_no in range(0, numbers_no):
  random_number = random.choice(numbers)
  password_list.append(random_number)

for  s_no in range(0, symbols_no):
  random_number = random.choice(symbols)
  password_list.append(random_number)

print(f"Password will contain : {password_list}")
 
random.shuffle(password_list)

final_pass = ""
for p in password_list:
  final_pass += p

print(f"PASSWORD GENERATED : {final_pass}")