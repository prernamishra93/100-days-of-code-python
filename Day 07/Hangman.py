import random
from Hangman_words import word_list
from Hangman_art import stages,logo

print(logo)
#TODO - 1 : Randomly choose a word from word_list and assign it to variable.
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ''
for letter in chosen_word:
    placeholder += '_'
print(f'Word to guess : {placeholder}')

game_over = False
correct_letter = []

lives = 6
while not game_over:
    print(f'***************************{lives}/6 LIVES LEFT ***************************')
    guess = input('\nTo win, guess the word before the person is hung.\n').lower()

    if guess in correct_letter:
        print(f'You\'v already guessed {guess}')
    
    display = ''
    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not in the word. You lose a life.")
    
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
        print('***************************YOU WIN***************************')
    elif lives == 0:
        game_over = True
        print(f'***************************IT WAS {chosen_word}! YOU LOSE***************************')
