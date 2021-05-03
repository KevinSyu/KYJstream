from flask import request, send_from_directory, Flask
from framework_init import kyj_stream
from lib.retry import retry
from lib.check_login import check_login
from service.logs_service import LogsService
from lib.exception.log_datetime_format_exception import LogDatetimeFormatException
import json
  
app = Flask(__name__)

class LogsController:
  @kyj_stream.route('/logs', methods=['GET'])
  @check_login
  def index():
    args = request.args
    time_begin = args.get('time_begin')
    time_end   = args.get('time_end')
    names      = args.get('names')
    levels     = args.get('levels')
    keywords   = args.get('keywords')
    regex      = args.get('regex')
    
    service = LogsService()

    try:
      log_result_list = service.search_log_list(time_begin, time_end, names, levels, keywords, regex)
    except LogDatetimeFormatException as e:
      # return error status with 422 response when datetime conversion failed
      return json.dumps({
        "status": "error",
        "message" : e.message
      }), 422

    # when searching proccess is success
    return json.dumps({
      "status": "success", 
      "data": { 
        "logs": log_result_list 
      }
    })