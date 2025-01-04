import random
from Hangman_words import word_list
from Hangman_art import stages


#TODO - 1 : Randomly choose a word from word_list and assign it to variable.
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ''
for letter in chosen_word:
    placeholder += '_'
print(placeholder)

game_over = False
correct_letter = []

lives = 6

while not game_over:
    guess = input('\nTo win, guess the word before the person is hung.\n').lower()
    display = ''
    if guess not in chosen_word:
        lives -= 1
    
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += '_'
    print(display)

    print(stages[lives])

    if '_' not in display:
        game_over = True
        print('You won!')
    elif lives == 0:
        game_over = True
        print('You lose!')


