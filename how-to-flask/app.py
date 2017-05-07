import random
import string

from flask import (
    Flask,
    request,
    jsonify
)

# the object is the 'instance' of the app, created using `__name__`, which is
# the name of the module we're executing in : 'app'
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/gibberish", methods=["POST"])
def gibberish():
    """Returns random strings and nonsense.

    POST requests with the following format:
        {
            'num_words': 9,
            'max_length_words'
        }

    Returns:
        {
            'gibberish': 'iwebv dEWs'
        }
    """

    # We expect the request to have some requests parameters in a json blob.
    # let's extract those into a variable, which will be treated as a dict.
    input_data = request.json
    num_words = input_data.get('num_words')
    max_word_length = input_data.get('max_word_length')

    gibberish = ''
    for i in xrange(num_words):
        #  make sure u only choose positive numbers.
        length = random.choice(range(1, max_word_length + 1))

        word = ''
        for j in xrange(length):
            word += random.choice(string.ascii_letters)

        gibberish += word + ' '

    result = {
        'gibberish': gibberish
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run()