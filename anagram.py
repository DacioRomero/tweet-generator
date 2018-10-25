# Display an anagram of a provided word
import random


# TODO: Generate *real* anagrams
def generator(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)


if __name__ == '__main__':
    import sys

    print(generator(sys.argv[1]))
