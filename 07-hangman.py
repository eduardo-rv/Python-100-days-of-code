import random
word_list = ["aardvark", "baboon", "camel"]


chose_word = random.choice(word_list)
print(chose_word)


placeholder = ""
for position in range(len(chose_word)):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()


    display = ""
    for l in chose_word:
        if l == guess:
            display += l
            correct_letters.append(guess)
        elif l in correct_letters:
            display += l
        else:
            display += "_"


    print(display)
    
    if "_" not in display:
        game_over = True
        print("You win.")














