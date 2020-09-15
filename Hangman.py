import random

word_list = ['python', 'java', 'kotlin', 'javascript']
flag = True

print("H A N G M A N")

while flag:
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == 'play':
        flag = True
        random_word = list(random.choice(word_list))
        progress = list('-' * len(random_word))
        lives = 8
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        typed_letters = set()

        while lives > 0:
            print(f"\n{''.join(progress)}")
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print('You should input a single letter')
                continue
            if letter not in alphabet:
                print('It is not an ASCII lowercase letter')
                continue
            if letter in typed_letters:
                print('You already typed this letter')
                continue
            typed_letters.add(letter)
            if letter in set(random_word):
                for i in range(len(random_word)):
                    if letter == random_word[i]:
                        progress[i] = letter
                        if progress == ''.join(random_word):
                            print('You guessed the word', progress)
                            break
            else:
                print("No such letter in the word")
                lives -= 1
        else:
            print('You are hanged!')
    if choice == 'exit':
        break
    else:
        continue
