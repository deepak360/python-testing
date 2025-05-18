from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Flask app!'})

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Missing input'}), 400
    return jsonify({'result': a + b})

if __name__ == '__main__':
    app.run(debug=True)
