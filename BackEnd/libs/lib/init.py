from lib.config import KYJStreamConfig

class KYJStreamInit:

  @staticmethod
  def init ():
    print('========== KYJStream init start ==========')
    KYJStreamConfig.init()
    print('========== KYJStream init end ==========')