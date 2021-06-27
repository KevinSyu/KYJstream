from flask import Flask,Blueprint
from lib.config import KYJStreamConfig
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
import datetime

kyj_stream = Blueprint('kyj-stream',__name__)

import controller.test_controller 
import controller.logs_controller
import controller.register_controller
import controller.rooms_controller
import error_handler

class FrameWork:
  jwt_config_section = 'kyjstream.secret.config'
  ___app = None

  @staticmethod
  def init():
    jwt = JWTManager()
    app = Flask(__name__)
    CORS(app)
    app.config['JWT_SECRET_KEY'] = KYJStreamConfig.get_str(FrameWork.jwt_config_section,'SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=KYJStreamConfig.get_int(FrameWork.jwt_config_section,'ACCESS_TOKEN_EXPIRES_TIME_IN_MINUTES'))
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=KYJStreamConfig.get_int(FrameWork.jwt_config_section,'REFRESH_TOKEN_EXPIRES_TIME_IN_DAYS'))
    jwt.init_app(app)
    app.register_blueprint(kyj_stream,url_prefix='/kyj_stream')
    FrameWork.__app = app

  @staticmethod
  def get_app():
    return FrameWork.__app
 
