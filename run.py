import random
from word_list import word_list
from lives_stages import lives_lost
import string

name = input("Please enter your name: -->")
print("Welcome to the the gallows ", name, "!!!!!")
print("==========================================")
print("To save your life try to guess the word in 7 attempts")

"""
Create a command to select a word from the word list.
Ensure that the word is a ful word with no '' or '-'.
"""


def get_only_valid(word_list):
    valid = random.choice(word_list) #   Randomly choose a word from the list
    while ' - ' in word or ' ' in word:
        word = random.choice(word_list)
    
    return word.upper()


def hangman():
    word = get_only_valid(word_list)
    letter_in_word = set(word)  #   Letters in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()