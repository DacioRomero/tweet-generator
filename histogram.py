# Generate a histogram of the frequency of words in a text
import re

word_re = re.compile(r'[a-zA-Z]+')


def histogram(source_text):
    '''Generates a histogram of a string.

    Args:
        source_text: The string to generate from.

    Returns:
        A dictonary of unique words with values of the number of occurences.
    '''
    words = [word.lower() for word in word_re.findall(source_text)]
    histogram = {}

    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram


def unique_words(histogram):
    '''Counts the number of unique words in a histogram.

    Args:
        histogram: The histogram (dictonary) to check.

    Returns:
        The number of unique words in the histogram.
    '''
    return len(histogram)


if __name__ == '__main__':
    with open('test.txt') as f:
        file_contents = f.read()

    histogram = histogram(file_contents)
    unique_words = unique_words(histogram)

    print(histogram)
    print(unique_words)
