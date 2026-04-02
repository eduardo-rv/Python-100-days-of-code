import random

letters = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z'
           ]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
word = []

print("Welcome to the PyPassword Generator!\n")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))

for n in range(0 ,nr_letters):
    word += random.choice(letters)

for n in range(0 ,nr_symbols):
    word += random.choice(numbers)

for n in range(0 ,nr_numbers):
    word += random.choice(symbols)

random.shuffle(word)


password = ""
for w in word:
    password += w

print(password)
