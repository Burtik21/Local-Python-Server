from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    data = request.json
    number = data.get('number')

    # Zpracování přijatých dat
    print(f'Přijaté číslo: {number}')

    return jsonify({'message': 'Data received successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)