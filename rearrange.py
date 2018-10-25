import sys
import random


def randomize_list(l):
    new_list = l[:]
    random.shuffle(new_list)
    return new_list


if __name__ == '__main__':
    args = sys.argv[1:]
    print(' '.join(randomize_list(args)))
