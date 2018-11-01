'''Display a random word from input based on frequency'''
import random
import sys
import histogram

def random_choice(the_histogram):
    '''Picks a weighted random choice from a histogram.

    Args:
        the_histogram: The histogram in dictionary format to choose from.

    Returns:
        A random choice using the frequency as the weights from the probability.
    '''
    return random.choices([*the_histogram], weights=the_histogram.values())[0]


def main():
    '''Tests random_choice().'''
    my_histogram = histogram.generate_histogram_dict(' '.join(sys.argv[1:]))
    print(random_choice(my_histogram))

if __name__ == '__main__':
    main()
