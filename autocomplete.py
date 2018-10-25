# Display all possible endings of the ending of a provided word
import sys
import dictionary_words


def autocomplete(string):
    dictionary = dictionary_words.get_dictionary()
    possibilities = [word for word in dictionary
                     if word.lower().startswith(string.lower())]

    return possibilities


if __name__ == '__main__':
    words = sys.argv[1]
    print('\n'.join(autocomplete(word)))
