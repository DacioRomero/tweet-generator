import sys
from flask import Flask
sys.path.insert(0, './coursework/Code')
import histogram
# from dictogram import Dictogram
from listogram import Listogram

def create_app():
    app = Flask(__name__)

    with open('./corpus.txt') as file:
        my_text = file.read()

    # app.histogram = Dictogram(histogram.get_words(my_text))
    app.histogram = Listogram(histogram.get_words(my_text))

    @app.route("/")
    def random_sentence():  #
        return ' '.join(app.histogram.samples(25))

    return app
