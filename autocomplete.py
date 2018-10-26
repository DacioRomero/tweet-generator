# Display all possible endings of the ending of a provided word
import dictionary_words
import sys


def fuzzy_startswith(string1, string2):
    '''Checks if one string starts with another regardless of case.

    Args:
        string1: A string which will be checked.
        string2: A string that is checked if string1 starts with.

    Returns:
        True if string1 starts with string2 otherwise False.
    '''
    return string1.upper().startswith(string2.upper())


def autocomplete(word):
    '''Creates list of words that finish the provided word.

    Args:
        word: A string representing the beginning of a words.

    Returns:
        A list of the different full representations of the word.
    '''
    dictionary = dictionary_words.get_dictionary()
    possibilities = list(filter(lambda w: fuzzy_startswith(w, word),
                                dictionary))

    return possibilities


if __name__ == '__main__':
    word = sys.argv[1]
    print('\n'.join(autocomplete(word)))
