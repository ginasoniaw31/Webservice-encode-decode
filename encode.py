from flask import Flask, request
import jwt

app = Flask(__name__)


@app.route('/api/v1/tambah', methods=['POST'])
def tambah():
    req = request.json
    encoded = req['enc']

    key = 'ginasonia'

    decoded = jwt.decode(encoded, key, "HS256")

    #return str(decoded['n1'])

    number1 = decoded['n1']
    number2 = decoded['n2']

    result = int(number1) + int(number2)

    return str(result)

@app.route('/api/v1/encode', methods=['POST'])
def enkode():
    req = request.json

    key = 'ginasonia'

    encoded = jwt.encode(
        {"n1": req['n1'], "n2": req['n2']}, key, "HS256")

    return str(encoded)



if __name__ == '__main__':
   app.run(debug = True, port=7007)