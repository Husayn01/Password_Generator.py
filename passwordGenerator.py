import random

letters = ['a','b','c','d','e','f','g','h''i','j','k','l','m','n','o','p','q','qr','s','t','u','w','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['@','#','$','%','^','&','*','?']

print("Password Generator")
numLetters = int(input("How many letters would you like?\n"))
numNumbers = int(input("How many numbers would you like?\n"))
numSymbols = int(input("How many symbols would you like?\n"))

password = []
for letter in range(1, numLetters + 1):
    randomLetters = random.choice(letters)
    password.append(randomLetters)
for num in range(1, numNumbers + 1):
    randomNum = random.choice(numbers)
    password.append(randomNum)
for num in range(1, numSymbols + 1):
    randomSymbols = random.choice(symbols)
    password.append(randomSymbols)

random.shuffle(password)
newPassword = ''
for char in password:
    newPassword += char
print(f"Your password is: {newPassword}")