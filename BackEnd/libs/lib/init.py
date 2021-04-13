from lib.config import KYJStreamConfig
from lib.log import KYJStreamLogger
class KYJStreamInit:

  @staticmethod
  def init ():
    print('========== KYJStream init start ==========')
    KYJStreamConfig.init()
    KYJStreamLogger.init()
    
    print('========== KYJStream init end ==========')