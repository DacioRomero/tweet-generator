# Display all possible endings of the ending of a provided word
import dictionary_words


def fuzzy_startswith(string1, string2):
    '''Check if string1 starts with string2 regardless of case'''
    return string1.upper().startswith(string2.upper())


def autocomplete(word):
    '''Return a list of words that finish the provided word'''
    dictionary = dictionary_words.get_dictionary()
    possibilities = list(filter(lambda w: fuzzy_startswith(w, word),
                                dictionary))

    return possibilities


if __name__ == '__main__':
    import sys

    word = sys.argv[1]
    print('\n'.join(autocomplete(word)))
