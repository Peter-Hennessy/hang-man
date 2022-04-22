import random
from word_list import word_list
from lives_stages import lives_lost
import string

name = input("Please enter your name: -->")
print("Welcome to the the gallows ", name, "!!!!!")
print("==========================================")
print("To save your life try to guess the word in 7 attempts")



def get_only_valid(word_list):
    valid = random.choice(word_list)   #   Randomly choose a word from the list
    while ' - ' in valid or ' ' in valid:
        word = random.choice(word_list)
    
    return word.upper()


def hangman():
    word = get_only_valid(word_list)
    letter_in_word = set(word)  #   Letters in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()

    lives = 7

    # Getting the input fromt the player
    while len(letter_in_word) > 0 and lives > 0:
        #  letters guessed
        print(
            "you have: ", 
            lives, "lives left and you have guessed these letters: ", ''.join(
                guessed_letters))
        
        #  Show the guessed word with correct letters and blanks
        complete_word = [letter if letter in guessed_letters else '-' for letter in valid]
        print(lives_lost[lives])
        print("Current word is: ", ' '.join(word_list))

        player_guess = input("Pick a letter: ").upper()
        if player_guess in alphabet - guessed_letters:
            guessed_letters.add(player_guess)
            if player_guess in letter_in_word:
                letter_in_word.remove(player_guess)
                print('')