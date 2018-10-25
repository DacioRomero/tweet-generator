import sys
import random


def randomize_list(input_list):
    output_list = input_list[:]
    random.shuffle(output_list)
    return output_list


if __name__ == '__main__':
    input_list = sys.argv[1:]
    print(' '.join(randomize_list(input_list)))
