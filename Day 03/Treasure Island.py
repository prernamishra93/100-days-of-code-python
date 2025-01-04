print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')
print("You're at a cross road. Where do you want to go?")
direction = input("Type 'Left' or 'Right'\n").lower()

if direction == 'left':
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == 'wait':
        choice3 = input("You arrived at the island unharmed. "
                        "There is house with 3 doors. "
                        "One Red, One Yellow and one blue. "
                        "Which color do you choose\n").lower()
        if choice3 == 'red':
            print("It's a room full of fire. Game Over.")
        elif choice3 == 'yellow':
            print("You found the treasure. You Win!")
        elif choice3 == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exists. Game Over.")
    else : 
        print("You got attacked by an angry trout. Game Over.")
else:
    print('You fell in the hole. Game Over.')

