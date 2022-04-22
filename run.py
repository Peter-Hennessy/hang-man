import random
from list_of_words import list_of_words
from lives_stages import lives_lost
import string


def get_valid_word(list_of_words):
    word = random.choice(list_of_words)   #   Randomly choose a word from the list
    while ' - ' in word or ' ' in word:
        word = random.choice(list_of_words)

    return word.upper()


def hangman():
    word = get_valid_word(list_of_words)
    letter_in_word = set(word)  #   Letters in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()

    lives = 7

    # Getting the input fromt the player
    while len(letter_in_word) > 0 and lives > 0:
        #  letters guessed
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(
            "you have: ",
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
        print("Undertaker take him away, the word was", word)
    else:
        print("\nYou have a last minute pardon, you geussed", word, "")


if __name__ == '__main__':
    hangman()
