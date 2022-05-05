"""
Create a game where the player must guess a word that is randomly selected
if a guess is wrong the player looses a life and a hangman image wil update
The player will have 8 lives to guess the word
"""
import random
import string
from list_of_words import list_of_words
from lives_stages import lives_lost


#    Randomly choose a word from the list

#  Only choose a valid word that does not contain ' - ' OR ' '
#  Return the fully guessed word in uppercase


def get_valid_word(list_of_words):
    word = random.choice(
        list_of_words)
    while ' - ' in word or ' ' in word:
        word = random.choice(list_of_words)

    return word.upper()

#   Letters in the word


def hangman():
    word = get_valid_word(list_of_words)
    letter_in_word = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()

    lives = 8

    # Getting the input fromt the player
    while len(letter_in_word) > 0 and lives > 0:
        #  letters guessed
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(
            "You have: ",
            lives, "lives left and you have guessed these letters: ", ' '.join(
                guessed_letters))

        #  Show the guessed word with correct letters and blanks
        word_list = [
            letter if letter in guessed_letters else '-' for letter in word]
        print(lives_lost[lives])
        print("Current word is: ", ' '.join(word_list))

        player_guess = input("Pick a letter: ").upper()
        if player_guess in alphabet - guessed_letters:
            guessed_letters.add(player_guess)
            if player_guess in letter_in_word:
                letter_in_word.remove(player_guess)
                print(' ')

            else:
                lives = lives - 1
                print(
                    "\nYour are incorrect", player_guess, "is not in the word"
                    )

        elif player_guess in guessed_letters:
            print("\nYou have already guessed tha letter, Please try again!")

        else:
            print("\nThat is not a valid letter.")

    #  Returns to here when len(letters-in_word) == 0 OR when lives == 0
    if lives == 0:
        print(lives_lost[lives])
        print("Undertaker take", name,  "away, the word was", word)
    else:
        print(
            "\nYou have a last minute pardon", name, "you guessed", word,
            "You are free to go!")


name = input("Please enter your name: -->  ")
print("Welcome to the gallows", name, "Hope you get home safe!!!")
print("=========================================================")
print("Try to guess the word in 8 attempts")


if __name__ == '__main__':
    hangman()
