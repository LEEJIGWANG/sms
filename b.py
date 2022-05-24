from flask import Flask, make_response, jsonify, request
import requests, json

app = Flask(__name__)
app.config['JSON_AS_ASCLL'] = False

@app.route('/', methods=['GET', 'POST'])
def hello():
    print(request.is_json)
    data = request.get_json()
    print(data)
    res = requests.post(' http://127.0.0.1:5000/text1', json=data['contents'])
    print(res.text)
    #return jsonify({"cal_result": machineResult})
    return res.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)