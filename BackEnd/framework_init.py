from flask import Flask,Blueprint

app = Flask(__name__)
kyj_stream = Blueprint('kyj-stream',__name__)

import controller.test_controller 

class FrameWork:

  @staticmethod
  def init():
    app.register_blueprint(kyj_stream,url_prefix='/kyj_stream')
    
    app.run(debug=True, host='127.0.0.1', port=8888)
 
