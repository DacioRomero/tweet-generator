# Display a random psuedo sentence
import random
import sys


def get_dictionary():
    '''Creates a list of words

    Args: None

    Returns:
        A list of words from the OSX dictionary
    '''
    with open('/usr/share/dict/words') as f:
        raw_file = f.read()
    return raw_file.splitlines()


def random_sentence(dictionary, num_words):
    '''Create a "sentence"

    Args:
        dictionary: A list of words from which the sentence will be
            constructed.
        num_words: An int of the number of words in the sentence.

    Returns:
        A "sentence" from words in dictionary with num_words number of words.
    '''
    return ' '.join(random.choice(dictionary) for _ in range(num_words))


if __name__ == '__main__':
    num_words = int(sys.argv[1])
    print(random_sentence(get_dictionary(), num_words))
