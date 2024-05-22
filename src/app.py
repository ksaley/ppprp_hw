from flask import Flask
import datetime

app = Flask(__name__)

request_counts = 0

@app.route('/time', methods=['GET'])
def time():
    global request_counts
    request_counts += 1
    return str(datetime.datetime.now())

@app.route('/statistics', methods=['GET'])
def statistics():
    return str(request_counts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)