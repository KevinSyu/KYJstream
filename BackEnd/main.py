from flask import Flask
from lib.init import KYJStreamInit
from lib.config import KYJStreamConfig
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask Dockerized TEST'


if __name__ == "__main__":
    KYJStreamInit.init()
    KYJStreamConfig.init()

    print(KYJStreamConfig.get_str('kyjstream.test','projectName'))
    # app.run(debug=True, host='0.0.0.0', port=8888)