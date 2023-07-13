from flask import Flask, request, jsonify
import syllables
import cmudict

app = Flask(__name__)

# Load the CMU Pronouncing Dictionary
cmu_dict = cmudict.dict()

@app.route("/")
def home():
    # Endpoint for root route
    return '<p>SEND A POST REQUEST TO /syllable WITH JSON BODY IN THIS FORMAT: {"word": "example"}<p>'

@app.route('/syllable', methods=['POST'])
def get_syllable_count():
    # Get the word from the JSON payload in the POST request
    word = request.json['word']

    # Count syllables using CMU Pronouncing Dictionary
    count = get_syllable_count_cmudict(word)

    # If the word is not found in CMU Pronouncing Dictionary, fall back to syllables library
    if count is None:
        count = syllables.estimate(word)

    # Return the syllable count as a JSON response
    return jsonify({'syllables': count})

def get_syllable_count_cmudict(word):
    # Check if the word is in the CMU Pronouncing Dictionary
    phones = lookup_word(word)
    if phones:
        # Select the first pronunciation and count the number of vowels (digits at the end of each phoneme)
        phones0 = phones[0]
        return len([p for p in phones0 if p[-1].isdigit()])

    # Word not found in CMU Pronouncing Dictionary
    return None

def lookup_word(word):
    # Look up the word in the CMU Pronouncing Dictionary, converting it to lowercase
    return cmu_dict.get(word.lower())

if __name__ == '__main__':
    app.run()
