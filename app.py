from flask import Flask
import sample
import histogram

app = Flask(__name__)

@app.route("/")
def hello():
    with open('./texts/test.txt') as file:
        my_text = file.read()

    my_histogram = histogram.generate_histogram_dict(my_text)
    return ' '.join(sample.histogram_samples(my_histogram, k=25))