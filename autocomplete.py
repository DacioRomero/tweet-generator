import sys
import dictionary_words


def autocomplete(string):
    dictionary = dictionary_words.get_dictionary()
    possibilities = [word for word in dictionary
                     if word.lower().startswith(string.lower())]

    return possibilities


if __name__ == '__main__':
    print('\n'.join(autocomplete(sys.argv[1])))
