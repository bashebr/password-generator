import random

chars = 'ábcdefghijklmnopqrstuvxyz1234567890!@#$%ˆ&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ'
passwordNumbers = input('How many password do you want to generate')
passwordNumbers = int(passwordNumbers)
length = input('Enter length of password you need to generate')
length = int(length)
for p in range(passwordNumbers):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)
