import random

def hangman():
    word_list = ["snake", "shark", "rabbit", "duck", "squirrel", "wolf",
                 "whale", "frog", "fox", "bear", "tiger", "lion", "cheeta",
                 "goose", "mongoose", "chicken", "bull", "buffalo"]
    random_number = random.randint(0,17)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["",
              "_______       ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     "]
    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    print("Hint: It's an animal")
    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter:")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((''.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '_' not in letter_board:
            print('You win! The word was:')
            print(''.join(letter_board))
            input("Press ENTER to exit")
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The word was {}'.format(word))
        input("Press ENTER to exit")

hangman()
    
