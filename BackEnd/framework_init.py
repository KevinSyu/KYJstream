from flask import Flask,Blueprint
from lib.config import KYJStreamConfig
from flask_jwt_extended import JWTManager
import os

kyj_stream = Blueprint('kyj-stream',__name__)

import controller.test_controller 
import error_handler

class FrameWork:
  jwt_config_section = 'kyjstream.secret.config'

  @staticmethod
  def init():
    jwt = JWTManager()
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = KYJStreamConfig.get_str(FrameWork.jwt_config_section,'SECRET_KEY')
    jwt.init_app(app)
    app.register_blueprint(kyj_stream,url_prefix='/kyj_stream')
    app.run(debug=True, host=KYJStreamConfig.get_host(), port=8888)
    

 
