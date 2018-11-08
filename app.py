from flask import Flask
import sys
sys.path.insert(0, 'coursework/Code')
sys.path.insert(0, 'coursework/Code/Python-Tools')
from dictogram import Dictogram
import histogram

app = Flask(__name__)

with open('./corpus.txt') as file:
    my_text = file.read()

my_dictogram = Dictogram(histogram.get_words(my_text))

@app.route("/")
def random_sentence():  #
    '''Root route for webapp'''
    return ' '.join(my_dictogram.samples(25))
