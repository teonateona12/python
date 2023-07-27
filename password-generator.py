import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print('Welcome to the PyPassword Generator!')

num_lettert = int(input('How many letters would you like in your password?'))
num_symbols = int(input('How many symbols would you like?'))
num_numbers = int(input('How many numbers would you like?'))

password_list = []
for char in range(1, num_numbers+1):
    password_list += random.choice(numbers)
for char in range(1, num_lettert+1):
    password_list += random.choice(letters)
for char in range(1, num_symbols+1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password+= char

print(f'Yor password is {password}')