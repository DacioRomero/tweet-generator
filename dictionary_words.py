import sys
import random


def get_dictionary():
    with open('/usr/share/dict/words') as f:
        raw_file = f.read()
    return raw_file.splitlines()


def random_sentence(dictionary, length):
    return ' '.join(random.choice(dictionary) for _ in range(length))


def main():
    print(random_sentence(get_dictionary(), int(sys.argv[1])))


if __name__ == '__main__':
    main()
