# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code

import random
import string


WORDLIST_FILENAME = "words.txt"
VOWELS = {'a', 'e', 'i', 'o', 'u'}
HINT = '*'
UNDERLINING = '_'
GUESSES_REMAINING = 6
WARNINGS_REMAINING = 3


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return True
    return False


def is_letter_guessed(secret_word, intended_letter):
    '''
    intended_letter: string, the intended letter entered by the user;
    secret_word: string, the word the user is guessing;
    returns: boolean, True if the user's intended letter is in secret_word;
        False otherwise
    '''
    return intended_letter in secret_word


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    open_letters = []
    for letter in secret_word:
        if letter in letters_guessed:
            open_letters.append(letter)
        else:
            open_letters.append('_ ')
    open_letters_str = ''.join(open_letters)
    return open_letters_str


def get_available_letters(intended_letter, available_letters):
    '''
    intended_letter: string, the intended letter entered by the user;
    available_letters: list of letters that have not yet been used;
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    if intended_letter in available_letters:
        available_letters = available_letters.replace(intended_letter, '')
    return available_letters
    
    
def hints_question():
    '''
    return: boolean, True if the value of the answer variable is "y", 
            otherwise returns False.
    '''
    
    # is_not_valid: boolean, until the condition is met, the value of the variable is True.  
    is_not_valid = True

    print('Do you want to play with hints?')
    while is_not_valid:
        # answer: string, the value entered by the user.  
        answer = input('If yes, enter "Y", if not, enter "N": ').lower()
        if answer not in ('y', 'n'):
            print('You have entered an incorrect value!')
        elif answer == 'y':
            return True
        else:
            return False


def start_game(secret_word):
    '''
    secret_word: string, the word the user is guessing;
    The function displays the user initial information about the beginning of the game 
    and the length of secret_word
    returns: boolean, the value of the answer True or False. 
            If True - hints will be used, if False - will not be used.
    '''
    print(f'Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print('You have 3 warnings left.')
    print('-------------')
    return hints_question()


def inf_for_user(intended_letter, guesses_remaining, secret_word, available_letters):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    guesses_remaining: integer, the number of attempts remaining to guess
    secret_word: string, the word the user is guessing;
    available_letters: list of letters that have not yet been used;
    The function displays the user information on how many attempts are left to guess 
    and which letters are available for guessing.
    '''
    available_letters = ''.join(available_letters)
    print(f'You have {guesses_remaining} guesses left.')
    print(f'Available letters: {available_letters}')


def warnings_left(warnings_remaining, secret_word, letters_guessed):
    '''
    warnings_remaining: integer, the number of warnings remaining;
    secret_word: string, the word the user is guessing;
    letters_guessed: list (of letters), which letters have been guessed so far;
    '''
    print(f'You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
    print('-------------')


def not_valid_letter(warnings_remaining, secret_word, letters_guessed):
    '''
    warnings_remaining: integer, the number of warnings remaining;
    secret_word: string, the word the user is guessing;
    letters_guessed: list (of letters), which letters have been guessed so far;
    The function displays information to the user that he has entered an invalid value, 
    as well as the number of remaining warnings and guessed letters in the word;
    '''
    print('Oops! That is not a valid letter.')
    warnings_left(warnings_remaining, secret_word, letters_guessed)


def already_guessed_letter(warnings_remaining, secret_word, letters_guessed):
    '''
    warnings_remaining: integer, the number of warnings remaining;
    secret_word: string, the word the user is guessing;
    letters_guessed: list (of letters), which letters have been guessed so far;
    The function displays the user information that he has entered a previously entered letter, 
    as well as the number of remaining warnings and guessed letters in the word;
    '''
    print(f"Oops! You've already guessed that letter.") 
    warnings_left(warnings_remaining, secret_word, letters_guessed)


def warnings_remaining_alphabet(warnings_remaining, secret_word, letters_guessed):
    '''
    warnings_remaining: integer, the number of warnings remaining;
    secret_word: string, the word the user is guessing;
    letters_guessed: list (of letters), which letters have been guessed so far;
    returns: The function subtracts one warning if their number was not equal to zero and returns it.
        Also displays the reason for subtracting the warning: Invalid value entered.;
    '''
    if warnings_remaining != 0:
        warnings_remaining -= 1
        not_valid_letter(warnings_remaining, secret_word, letters_guessed)
    return warnings_remaining


def guesses_remaining_alphabet(guesses_remaining, warnings_remaining, secret_word, letters_guessed):
    '''
    guesses_remaning: integer, the number of attempts remaining to guess;
    warnings_remaining: integer, the number of warnings remaining;
    secret_word: string, the word the user is guessing;
    letters_guessed: list (of letters), which letters have been guessed so far;
    returns: The function subtracts one guess and returns it. 
        Also displays the reason for the subtraction guess: Invalid value entered;
    '''
    if warnings_remaining == 0:
        guesses_remaining -= 1
        not_valid_letter(warnings_remaining, secret_word, letters_guessed)
    return guesses_remaining


def warnings_remaining_letters_guessed(warnings_remaining, secret_word, letters_guessed):
    '''
    warnings_remaining: integer, the number of warnings remaining;
    secret_word: string, the word the user is guessing;
    letters_guessed: list (of letters), which letters have been guessed so far;
    returns: The function subtracts one warning if their number was not equal to zero and returns it.
        Also displays the reason for subtracting the warning: The letter is re-entered;
    '''
    if warnings_remaining != 0:
        warnings_remaining -= 1
        already_guessed_letter(warnings_remaining, secret_word, letters_guessed)
    return warnings_remaining


def guesses_remaining_letters_guessed(warnings_remaining, guesses_remaining, secret_word, letters_guessed):
    '''
    guesses_remaning: guesses_remaining: integer, the number of attempts remaining to guess
    warnings_remaining: integer, the number of warnings remaining;
    secret_word: string, the word the user is guessing;
    letters_guessed: list (of letters), which letters have been guessed so far;
    returns: The function subtracts one guess and returns it. 
        Also displays the reason for the subtraction guess: The letter is re-entered;
    '''
    if warnings_remaining == 0:
        guesses_remaining -= 1
        already_guessed_letter(warnings_remaining, secret_word, letters_guessed)
    return guesses_remaining 


def good_guess(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing;
    letters_guessed: list (of letters), which letters have been guessed so far;
    The function displays to the user the information that he guessed the letter and the guessed letters in the word.
    '''
    print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
    print('-------------')


def win_score_and_loose(guesses_remaining, secret_word):
    '''
    guesses_remaning: integer, the number of attempts remaining to guess;
    secret_word: string, the word the user is guessing;
    The function displays the user's congratulations that he won and his score.
    '''
    if guesses_remaining == 0:
        print(f'Sorry, you ran out of guesses. The word was else: {secret_word}')
    else:
        score = guesses_remaining * len(set(secret_word))
        print(f'Congratulations, you won! Your total score for this game is: {score}')
    

def not_in_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing;
    letters_guessed: list (of letters), which letters have been guessed so far;
    The function displays to the user the information which has not guessed a letter, and the guessed letters in a word.
    '''
    print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
    print('-------------')


def check_vowels(intended_letter, guesses_remaining):
    '''
    intended_letter: string, the intended letter entered by the user;
    vowels: set (of vowels);
    guesses_remaining: integer, the number of attempts remaining to guess;
    returns: The function checks whether the entered letter is a vowel, 
        if there is - two attempts to guess are deducted, if not - one attempt is deducted;
        Returns the number of attempts;
    '''
    if intended_letter in VOWELS and guesses_remaining > 1:
        guesses_remaining -= 2
    else:
        guesses_remaining -= 1
    return guesses_remaining


def match_with_gaps(my_word_without_spaces, other_word):
    '''
    my_word_without_spaces: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True, if all the guessed letters are in the word. 
            False otherwise.
    '''
    if len(other_word) == len(my_word_without_spaces):
        for letter_in_my_word, letter_in_other_word in zip(my_word_without_spaces, other_word):
            if letter_in_my_word == UNDERLINING:
                if letter_in_other_word in my_word_without_spaces:
                    return False
                continue
            if letter_in_my_word == letter_in_other_word:
                continue
            return False
        return True
    return False


def show_possible_matches(my_word, secret_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    possible_matches = []
    my_word_without_spaces = my_word.replace(' ', '')

    for word in wordlist:
        if my_word_without_spaces == len(secret_word) * UNDERLINING:
            if match_with_gaps(my_word_without_spaces, word):
                possible_matches.append(word)
                possible_matches = possible_matches[0:50]
        if match_with_gaps(my_word_without_spaces, word):
            possible_matches.append(word)

    if not possible_matches:
        print('No matches found.')
    else:
        possible_matches = ' '.join(possible_matches)
        print(f'Possible word matches are: {possible_matches}')
    print('-------------')


def count_warnings_guesses_remainings(intended_letter, warnings_remaining, guesses_remaining, secret_word, letters_guessed):
    '''
    intended_letter: string, the intended letter entered by the user; 
    warnings_remaining: integer, the number of warnings remaining;
    guesses_remaining: integer, the number of attempts remaining to guess;
    secret_word: string, the secret word to guess.
    letters_guessed: list (of letters), which letters have been guessed so far;
    returns: warnings_remaining, guesses_remaining, boolean - True, an indication that the entered letter is incorrect, 
            False, letter is correct.
    '''
    if intended_letter not in string.ascii_letters:
        warnings_remaining = warnings_remaining_alphabet(warnings_remaining, secret_word, letters_guessed)
        guesses_remaining = guesses_remaining_alphabet(guesses_remaining, warnings_remaining, secret_word, letters_guessed)
        return warnings_remaining, guesses_remaining, True

    if intended_letter in letters_guessed:
        warnings_remaining = warnings_remaining_letters_guessed(warnings_remaining, secret_word, letters_guessed)
        guesses_remaining = guesses_remaining_letters_guessed(warnings_remaining, guesses_remaining, secret_word, letters_guessed)
        return warnings_remaining, guesses_remaining, True
    
    return warnings_remaining, guesses_remaining, False


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess
    '''
    guesses_remaining = GUESSES_REMAINING
    warnings_remaining = WARNINGS_REMAINING
    letters_guessed = set()
    intended_letter = ''
    available_letters = string.ascii_lowercase

    answer = start_game(secret_word)

    while is_word_guessed(secret_word, letters_guessed) and guesses_remaining > 0:
        available_letters = get_available_letters(intended_letter, available_letters)
        inf_for_user(intended_letter, guesses_remaining, secret_word, available_letters)
        intended_letter = input('Please guess a letter: ').lower()

        if answer and intended_letter == HINT:
            show_possible_matches(get_guessed_word(secret_word, letters_guessed), secret_word)
            continue

        not_correct_letter = False
        warnings_remaining, guesses_remaining, not_correct_letter = \
        count_warnings_guesses_remainings(intended_letter, warnings_remaining, guesses_remaining, 
                                        secret_word, letters_guessed)
        
        if not_correct_letter:
            continue
        
        letters_guessed.add(intended_letter)
        
        if is_letter_guessed(secret_word, intended_letter):
            good_guess(secret_word, letters_guessed)
            continue
        not_in_word(secret_word, letters_guessed)
        guesses_remaining = check_vowels(intended_letter, guesses_remaining)

    win_score_and_loose(guesses_remaining, secret_word)


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)