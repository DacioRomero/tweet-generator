# Display a shuffled version of a provided list without mutation
import random


def randomize_list(input_list):
    output_list = input_list[:]
    random.shuffle(output_list)
    return output_list


if __name__ == '__main__':
    import sys

    input_list = sys.argv[1:]
    print(' '.join(randomize_list(input_list)))
