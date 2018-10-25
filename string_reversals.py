# Display the reverse a word or sentence
def reverse_word(word):
    return word[::-1]


def reverse_sentence(sentence):
    return ' '.join(sentence.split(' ')[::-1])


if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'word':
        word = sys.argv[2]
        print(reverse_word(word))

    elif sys.argv[1] == 'sentence':
        sentence = ' '.join(argv[2:])
        print(reverse_sentence(sentence))
