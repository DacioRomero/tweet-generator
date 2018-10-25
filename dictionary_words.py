import sys
import random


def get_dictionary():
    with open('/usr/share/dict/words') as f:
        raw_file = f.read()
    return raw_file.splitlines()


def random_sentence(dictionary, num_words):
    return ' '.join(random.choice(dictionary) for _ in range(length))


if __name__ == '__main__':
    num_words = int(sys.argv[1])
    print(random_sentence(get_dictionary(), num_words))
