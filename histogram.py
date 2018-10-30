'''Generate a histogram of the frequency of words in a text'''
import re

# Matches latin-esque words
WORD_RE = re.compile(r'[a-zA-Z]+(?:\'[a-z]+)?')


def histogram(source_text):
    '''Generates a histogram of a string.

    Args:
        source_text: The string to generate from.

    Returns:
        A dictonary of unique words with values of the number of occurences.
    '''
    words = get_words(source_text)
    histogram = {}

    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram


def histogram_ll(source_text):
    '''Generates a histogram of a string.

    Args:
        source_text: The string to generate from.

    Returns:
        A list of lists of unique words with values of the number of occurences.
    '''
    words = get_words(source_text)
    words.sort()

    histogram = []
    for index, word in enumerate(words):
        if index > 0 and word == words[index - 1]:
            histogram[-1][1] += 1
        else:
            histogram.append([word, 1])

    return histogram

def get_words(source_text):
    '''Get the words in a text.

    Args:
        source_text: The string to parse.

    Returns:
        A list of strings of the words in a text.
    '''
    # Find all words using regex, make them lowercase, and put them in a list
    return [word.lower() for word in WORD_RE.findall(source_text)]


def unique_words(histogram):
    '''Counts the number of unique words in a histogram.

    Args:
        histogram: The histogram (dictonary) to check.

    Returns:
        The number of unique words in the histogram.
    '''
    return len(histogram)


if __name__ == '__main__':
    with open('./texts/test.txt') as file:
        file_contents = file.read()

    histogram = histogram_ll(file_contents)
    # unique_words = unique_words(histogram)

    print(histogram)
    # print(unique_words)
