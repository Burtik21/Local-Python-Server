from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/post-number', methods=['POST'])
def fun():
    data = request.json
    number = data.get('number')

    # Odeslání dat na druhý server
    second_server_response = requests.post('http://localhost:5001/receive', json={'number': number})

    return number

if __name__ == '__main__':
    app.run(debug=True, port=5000)