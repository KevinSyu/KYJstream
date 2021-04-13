from flask import Flask,Blueprint
import os

kyj_stream = Blueprint('kyj-stream',__name__)

import controller.test_controller 

class FrameWork:

  @staticmethod
  def init():
    app = Flask(__name__)
    app.register_blueprint(kyj_stream,url_prefix='/kyj_stream')
  
    if os.environ['ENVIRONMENT'] == "dockerdev":
      app.run(debug=True, host='0.0.0.0', port=8888)
    else:
      app.run(debug=True, host='127.0.0.1', port=8888)

 
