from flask import Flask

kyj_stream_api = Flask(__name__)

class FrameWork:

  @staticmethod
  def init():
    kyj_stream_api.run(debug=True, host='0.0.0.0', port=8888)
