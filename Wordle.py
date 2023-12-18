"""
Kat Basilio
Comp 112-04 Final Project
Wordle
"""
import random

def game_instruction():
    """
    sig: none -> str
    prints instructions for the game
    """
    print("""You have six attempts to guess a five letter hidden word 
Your Progress Guide "✅➕❌"  
"✅" Indicates that the letter at that position was guessed correctly 
"➕" indicates that the letter at that position is in the hidden word, but in a different position 
"❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """)

def word_picker():
    """
    sig: none -> str
    picks a random secret word
    """
    global secret_word
    word_bank = []
    with open("word_bank.txt") as word_file:
        for line in word_file:
            word_bank.append(line.rstrip().lower())
        secret_word = random.choice(word_bank)
    return secret_word

def double_letters(word):
    """
    sig: str -> bool 
    checks for double letters in a word
    """
    seen = []
    for char in word:
        if char in seen:
            return True
        seen.append(char)
    return False

def update_win(wins, total_games):
    """
    sig: int -> str
    updates the win ratio
    """
    win_ratio = wins / total_games 
    with open("win_ratio.txt", "w") as f:
        f.write(str(win_ratio))

def get_win():
    """
    sig: none -> float
    returns the win ratio
    """
    try:
        with open("win_ratio.txt", "r") as f:
            return float(f.read())
    except FileNotFoundError:
        return 0.0


def wordle_game():
    """
    main game loop
    """
    total_wins = 0
    total_games = 0

    while True:
        secret_word = word_picker()  
        attempt = 6

        if double_letters(secret_word):  ## checks if the secret word has double letters 
            print('Warning: The word has double letters!')

            
        while attempt > 0:
                
            guess = input("Guess the word: ").lower()  

            if double_letters(guess) == True and double_letters(secret_word) == False:  ## checks for double letters in guess
                print('Warning: Your guess has double letters, but the secret word does not!') 

            if guess.isalpha() and len(guess) == 5:  ## validates player's guess
                if guess == secret_word:
                    total_wins += 1
                    total_games += 1
                    update_win(total_wins, total_games)

                    print('Win ratio:', get_win())  ## displays win ratio
                    again = input("You guessed the word correctly! 🎉 Play again? (yes/no) ").lower()

                    if again == 'yes':
                        break  ## breaks inner loop to restart game
                    elif again == 'no':
                        return ## returns from function to quit game 
                    else:
                        again = input('Please answer yes or no: ')
                        
                else:
                    attempt -= 1
                    print("You have", attempt, "attempt(s)")

                    for i in range(len(secret_word)):
                        char, word = secret_word[i], guess[i]  ## iterates over each character in both secret_word and guess, assigns variables respectively

                        if word == char:
                            print(word + " ✅ ")
                        elif word in secret_word:
                            print(word + " ➕ ")
                        else:
                            print(word + " ❌ ")

                    if attempt == 0:
                        total_games += 1
                        update_win(total_wins, total_games)

                        print('Win ratio:', get_win()) ## displays win ratio
                        again = input(f'You lost! 🚫 The word was: "{secret_word}". Play again? (yes/no) ').lower()

                        if again == 'yes':
                            break  ## breaks inner loop to restart the game
                        elif again == 'no':
                            return  ## returns from function to quit game
                        else:
                            again = input('Please answer yes or no: ')
            else:
                print("Not a valid guess. Please make sure to enter a five-letter word!")


game_instruction()
wordle_game()
