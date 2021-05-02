from flask import Flask,Blueprint
from lib.config import KYJStreamConfig
import os

kyj_stream = Blueprint('kyj-stream',__name__)

import controller.test_controller 
import controller.logs_controller
import error_handler

class FrameWork:

  @staticmethod
  def init():
    app = Flask(__name__)
    app.register_blueprint(kyj_stream,url_prefix='/kyj_stream')
    app.run(debug=True, host=KYJStreamConfig.get_host(), port=8888)


 
