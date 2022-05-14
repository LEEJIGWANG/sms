from flask import Flask, make_response, jsonify, request
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCLL'] = False

@app.route('/', methods=['GET', 'POST'])
def hello():
    data = request.get_json()
    file = open('hello.txt', 'w', encoding='utf8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write(str(data))            # 파일에 문자열 저장
    file.close()                     # 파일 객체 닫기
    print(data)
    files = open('hello.txt', 'rb')
    upload = {'file': files}
    res = requests.post(' http://127.0.0.1:5000/text', files = upload)
    return jsonify({'data':data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)