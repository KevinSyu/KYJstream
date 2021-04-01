from lib.config import KYJStreamConfig
import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime

class KYJStreamLogger:

  __log_path_section = 'kyjstream.config'

  @staticmethod
  def init():
    path = KYJStreamConfig.get_str(KYJStreamLogger.__log_path_section,'LOG_PATH')
    name = KYJStreamConfig.get_str(KYJStreamLogger.__log_path_section,'LOG_NAME')

    if not os.path.isdir(path):
      os.mkdir(path)
        
    logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S',
      handlers=[TimedRotatingFileHandler(path+str(datetime.today().date())+'-'+name, when='midnight'),
      TimedRotatingFileHandler(path+name, when='midnight')]
    )

    KYJStreamLogger.log_info('test')

  @staticmethod
  def log_info(msg):
    logging.info(msg)

  @staticmethod
  def log_warning(msg):
    logging.warning(msg)

  @staticmethod
  def log_error(msg):
    logging.error(msg)

  
