# Display a shuffled version of a provided list without mutation
import random
import sys


def randomize_list(input_list):
    '''Rearrange a list without mutation.

    Args:
        input_list: A list to be reversed.

    Returns:
        The randomly rearranged list.
    '''
    output_list = input_list[:]
    random.shuffle(output_list)
    return output_list


if __name__ == '__main__':
    input_list = sys.argv[1:]
    print(' '.join(randomize_list(input_list)))
