from flask import request, send_from_directory, Flask
from framework_init import kyj_stream
from service.test_service import TestService
from lib.retry import retry
from lib.check_login import check_login
from functools import wraps
from lib.exception.config_not_found_exception import ConfigNotFoundException

import os
from datetime import datetime
from lib.log import KYJStreamLogger
import re
import json
  
app = Flask(__name__)

class LogsController:
  @kyj_stream.route('/logs',methods=['GET'])
  @check_login
  def index():
    log_result = []

    args = request.args
    time_begin = args.get('time_begin')
    time_end   = args.get('time_end')
    names      = args.get('names')
    levels     = args.get('levels')
    keywords   = args.get('keywords')
    regex      = args.get('regex')
    
    log_result_list = LogsController.search_log_list(time_begin, time_end, names, levels, keywords, regex)

    return json.dumps({"data": log_result_list})
  
  @staticmethod
  def search_log_list(time_begin, time_end, names, levels, keywords, regex):
    log_list = LogsController.get_log_list()
    log_result_list = []

    # prepare variable for filtering time
    if time_begin:
      time_begin = datetime.strptime(time_begin, '%Y-%m-%d-%H:%M:%S')
    if time_end:
      time_end = datetime.strptime(time_end, '%Y-%m-%d-%H:%M:%S')
    
    # prepare variable for filtering name
    name_list = []
    if names:
      name_list = names.split(",")
    
    # prepare variable for filtering level
    level_list = []
    if levels:
      level_list = levels.split(",")

    # prepare variable for filtering keyword
    keyword_and_list = []
    keyword_or_list = []
    if keywords:
      if "&&" in keywords:
        keyword_and_list = keywords.split("&&")
      elif "||" in keywords:
        keyword_or_list = keywords.split("||")
      else:
        keyword_and_list = [keywords]

    # filter each log
    for log in log_list:

      log_time = datetime.strptime(log["time"], '%Y-%m-%d %H:%M:%S')
      if time_end and log_time > time_end:
        break
      if time_begin and log_time < time_begin:
        continue
      
      if not LogsController.is_list_match(log["name"], name_list):
        continue

      if not LogsController.is_list_match(log["level"], level_list):
        continue
      
      if not LogsController.is_keyword_match(log["msg"], keyword_and_list, keyword_or_list):
        continue

      if not LogsController.is_regex_match(log["msg"], regex):
        continue
      
      # add to result if everying matches
      log_result_list.append(log)

    return log_result_list
  

  @staticmethod
  def is_keyword_match(msg, keyword_and_list, keyword_or_list):
    if keyword_and_list:
      for keyword in keyword_and_list:
        if not keyword in msg:
          return False

    if keyword_or_list:
      if not any(keyword in msg for keyword in keyword_or_list):
        return False
        
    return True

  @staticmethod
  def is_regex_match(msg, regex):
    if regex:
      return (regex and re.match(r"{}".format(regex), msg))
    return True

  @staticmethod
  def is_list_match(log_item, item_list):
    if item_list:
      return any(log_item in item for item in item_list)
    return True

  @staticmethod
  def get_log_list():
    log_list = []

    log_file = open(os.path.join('log', 'system.log'))
    lines = log_file.readlines()

    for line in lines:
      line_split = line.split(' - ', 3)

      # check whether this line is a new log or not 
      # (by checking if line start with date)
      if re.match(r"^(\d+\D*){6}", line_split[0]):
        log_list.append({
          "time":  line_split[0].strip(),
          "name":  line_split[1].strip(),
          "level": line_split[2].strip(),
          "msg":   line_split[3].strip()
        })
      else:
        log_list[-1]["msg"] += line

    return log_list
  

#   @retry(exception=ConfigNotFoundException,times=2, delay=0)
#   def print_test(msg):
#     raise ConfigNotFoundException('config not found')