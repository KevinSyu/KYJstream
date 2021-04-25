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
  
app = Flask(__name__)

class LogsController:

  @kyj_stream.route('/logs',methods=['GET'])
  @check_login
  def index():
    log_list = []

    log_path = os.path.join('log', 'system.log')
    log_file = open(log_path)
    lines = log_file.readlines()

    # KYJStreamLogger.log_info(type(lines))

    for line in lines:
        line_split = line.split(' - ', 3)

        # check whether this line is a new log or not
        if re.match(r"^(\d+\D*){6}", line_split[0]):
            log_list.append({
                "time":  line_split[0].strip(),
                "name":  line_split[1].strip(),
                "level": line_split[2].strip(),
                "msg":   line_split[3]
            })
        else:
            log_list[-1]["msg"] += line

    return request.args.get('keyword')

#   @retry(exception=ConfigNotFoundException,times=2, delay=0)
#   def print_test(msg):
#     raise ConfigNotFoundException('config not found')