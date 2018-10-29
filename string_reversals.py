'''Display the reverse a word or sentence'''
import sys


def reverse_word(word):
    '''Reverses a word.

    Args:
        word: The string representing a words.

    Returns:
        The variable word reversed.
    '''
    return word[::-1]


def reverse_sentence(sentence):
    '''Reverses a sentence's words.

    Args:
        sentence: A string of a sentence.
    Returns:
        A new sentence with the words of the setence reversed.``
    '''
    return ' '.join(sentence.split(' ')[::-1])


if __name__ == '__main__':
    if sys.argv[1] == 'word':
        word = sys.argv[2]
        print(reverse_word(word))

    elif sys.argv[1] == 'sentence':
        sentence = ' '.join(sys.argv[2:])
        print(reverse_sentence(sentence))
