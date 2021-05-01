from lib.config import KYJStreamConfig
import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime
from pytz import timezone
from flask.logging import default_handler


class KYJStreamLogger:

  __log_path_section = 'kyjstream.config'

  @staticmethod
  def init():
    path = KYJStreamConfig.get_str(KYJStreamLogger.__log_path_section,'LOG_PATH')
    name = KYJStreamConfig.get_str(KYJStreamLogger.__log_path_section,'LOG_NAME')

    if not os.path.isdir(path):
      os.mkdir(path)

    werkzeug_log = logging.getLogger('werkzeug')
    werkzeug_log.setLevel(logging.ERROR)
    
    logging.Formatter.converter = lambda *args: datetime.now(tz=timezone('Asia/Taipei')).timetuple()
    logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S',
      handlers=[
      TimedRotatingFileHandler(path+name, when='midnight')]
    )

  @staticmethod
  def log_info(msg):
    logging.info(msg)

  @staticmethod
  def log_warning(msg):
    logging.warning(msg)

  @staticmethod
  def log_error(msg,exception = None):
    if exception is None:
      logging.error(msg)
    else:
      logging.exception(msg)

  
