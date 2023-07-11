from flask import Flask, request, jsonify
import syllables

app = Flask(__name__)

@app.route('/syllables', methods=['POST'])
def count_syllables():
    word = request.json['word']
    syllable_count = syllables.estimate(word)
    return jsonify({'syllables': syllable_count})

if __name__ == '__main__':
    app.run()
