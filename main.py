"""
This is the HANGMAN game for 2-players or 1-player against the computer!

The game prompts player 1 to pick a word. Then the screen clear itself so that player 2 can't see the word

After the screen is clear, the "gallows" and the empty letter spaces should be drawn, and player 2 should
be allowed to guess letters until they either win, or lose. As they choose correct letters, the letters should
appear on the screen in place of the blank space (clear and redraw the whole screen). As they choose wrong letters,
the "man" himself should come end up being drawn, piece by piece. How many guesses they get before losing is up
to you (depending on how complicated of a man you want to draw).

For 1-Player game a dictionary is used.
When the game starts, the computer should pick a random word from the dictionary.
This will allow you to play against the computer instead of only 2-player mode.
When the game starts, the user is prompted to choose between 1-player or 2-player mode.

"""

import random
from getpass import getpass


def p2_input():
    entry = False
    while not entry:
        word = str(getpass("Hi Player 1, this is your turn. Choose a word to be guessed: ")).upper()
        if len(set(word)) <= 8:
            print(chr(27) + "[2J")
            print("\n"*28)
            return word
        else:
            print("\n")
            print("Sorry, nice try. But that is too hard to be guessed in 8 attempts! Try something else: ")
            entry = False


def comp_input():
    entry = False
    while not entry:
        lines = open("wordlist.txt").read().splitlines()
        word_raw = random.choice(lines).split("/")
        word = word_raw[0].upper()
        if len(set(word)) <= 8:
            return word
        else:
            entry = False


def choose_player():
    print("Welcome to a little game of HANGMAN!")
    mode = str(input("Do you want to play against the computer or another player? (c or p): "))
    if mode == "c":
        comp_input()
        secret = comp_input()
        return secret
    else:
        secret = p2_input()
        return secret


# update guess progress
def guess_update(character):
    guess = False
    for i in range(len(guess_index)):
        if character == guess_index[i]:
            current_index[i] = character
            guess = True
    if guess is False:
        return False
    elif "_" not in current_index:
        print(" ".join(current_index))
        print("We have a winner! Congratulations!")
        exit()
    else:
        return True
# hangman picture list for 6 rounds


hang_man_picture = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


guessword = choose_player()
guess_index = list(guessword)
g_length = len(guessword)
current_index = list("_" * len(guess_index))

# Let's start the guessing:
print("Hi Player1, let's start the guessing. You have 6 tries on total.")
counter = 6
while counter >= 0:
    if counter > 1:
        print("You have ", counter, " guesses left")
    elif counter == 1:
        print("You have ", counter, " guess left")
    else:
        print(hang_man_picture[6])
        play = input("Sorry, you have lost! The correct word was" + str(guessword) + ". Let's give it another try, ok? (y/n) ")
        if play == "n":
            exit()
        else:
            current_index = list("_" * len(guess_index))
            counter = 6
            guessword = choose_player()

    print(hang_man_picture[6-counter])
    print(" ".join(current_index))
    c = str(input("Enter a character: ")).upper()
    if guess_update(c) is False:
        counter -= 1
