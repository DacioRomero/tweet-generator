import sys


def reverse_word(word):
    return word[::-1]


def reverse_sentence(sentence):
    return ' '.join(sentence.split(' ')[::-1])


if __name__ == '__main__':
    if sys.argv[1] == 'word':
        print(reverse_word(sys.argv[2]))
    elif sys.argv[1] == 'sentence':
        print(reverse_sentence(' '.join(sys.argv[2:])))
