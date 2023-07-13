from flask import Flask, request, jsonify
import syllables
import cmudict

app = Flask(__name__)

cmu_dict = cmudict.dict()

@app.route("/")
def home():
    return '<p>SEND A POST REQUEST TO /syllables WITH JSON BODY IN THIS FORMAT: {"word": "example"}<p>'

@app.route('/syllable', methods=['POST'])
def get_syllable_count():
    word = request.json['word']
    count = get_syllable_count_cmudict(word)
    if count is None:
        count = syllables.estimate(word)
    return jsonify({'syllables': count})

def get_syllable_count_cmudict(word):
    phones = lookup_word(word)
    if phones:
        phones0 = phones[0]
        return len([p for p in phones0 if p[-1].isdigit()])
    return None

def lookup_word(word):
    return cmu_dict.get(word.lower())

if __name__ == '__main__':
    app.run()
