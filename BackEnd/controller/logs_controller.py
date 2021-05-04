from flask import request, send_from_directory, Flask
from framework_init import kyj_stream
from lib.retry import retry
from lib.check_login import check_login
from service.logs_service import LogsService
from lib.exception.log_datetime_format_exception import LogDatetimeFormatException
from lib.json_response import *
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
      # when datetime conversion failed, return status 422 with error message.
      return api_unprocessable_entity(e.message)

    # when searching proccess is success, return search result
    return api_success({"logs": log_result_list})