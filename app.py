from flask import Flask
import sample
import histogram

app = Flask(__name__)

@app.route("/")
def random_sentence():  #
    '''Root route for webapp'''
    with open('./texts/test.txt') as file:
        my_text = file.read()

    my_histogram = histogram.generate_histogram_dict(my_text)
    return ' '.join(sample.histogram_samples(my_histogram, k=25))

if __name__ == '__main__':
    app.run(debug=True)
