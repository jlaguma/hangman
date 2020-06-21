import random
import secrets
import string
import re
import sys
from os import system, name

from .words import words


def get_word():
    """Select a random word consisting only out of letters."""
    reg = re.compile('^[a-z]*$')
    word = secrets.SystemRandom().choice(words)
    while not reg.match(word):
        word = secrets.SystemRandom().choice(words)
    return word.upper()


def get_pic(n):
    """Hangman pics."""
    levels = [
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        --
        """, """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     /
        -
        """, """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |
        --
        """, """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |
        --
        """, """
        --------
        |      |
        |      O
        |      |
        |      |
        |
        --
        """, """
        --------
        |      |
        |      O
        |
        |
        |
        --
        """, """
        --------
        |      |
        |
        |
        |
        |
        --
        """
    ]
    return levels[n]


def get_output(tries, progress, guessed_letters):
    """Prints the output to the player."""
    if (tries == 6):
        clear()
        print(f'Good Luck!')
    print(get_pic(tries))
    print(f'You have {tries} tries left. You have used these letters: ',
          ' '.join(guessed_letters))
    print(f'\n{progress}')
    print()


def clear():
    """Clear the screen."""
    # for windows
    print(name)
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    print('\n' * 3)


def hangman():
    """Game loop."""
    try:
        answer = play(get_word())
        while input(f'{answer} Play Again? (Y/N) ').upper() == 'Y':
            answer = play(get_word())
    except:
        # catch ctrl+c / ctrl+z
        sys.exit()


def play(word):
    """Game logic."""
    progress = '_ ' * len(word)
    guessed_letters = []
    guessed_words = []
    guessed = False
    tries = 6
    get_output(tries, progress, guessed_letters)

    while not guessed and tries > 0:
        user_guess = input(f'Guess a letter or a word: ').upper()
        # guess a single letter
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in guessed_letters:
                clear()
                print(f'You already guessed the letter {user_guess}.')
            elif user_guess not in word:
                clear()
                print(f'Incorrect!')
                tries -= 1
                guessed_letters.append(user_guess)
            else:
                clear()
                print(f'Correct!!!')
                guessed_letters.append(user_guess)
                progress = ' '.join([
                    letter if letter in guessed_letters else '_'
                    for letter in word
                ])
                if '_' not in progress:
                    guessed = True
        # guess entire word
        elif len(user_guess) == len(word) and word.isalpha():
            if user_guess in guessed_words:
                print('You already guessed the word {user_guess}.')
            elif user_guess != word:
                clear()
                print(f'Incorrect!')
                tries -= 1
                guessed_words.append(user_guess)
            else:
                clear()
                print(f'Correct!!!')
                guessed = True
        else:
            clear()
            print(f'Incorrect!')
        get_output(tries, progress, guessed_letters)
    if guessed:
        return f'You are correct! The word was {word}.'
    else:
        return f'You are out of tries. The word was {word}.'


if __name__ == '__main__':
    hangman()
