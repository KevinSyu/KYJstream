from lib.config import KYJStreamConfig
from lib.log import KYJStreamLogger
class KYJStreamInit:

  __crypt_config_section = "kyjstream.secret.crypt"
  __crypt_config_key = "KEY"

  @staticmethod
  def init ():
    print('========== KYJStream init start ==========')
    KYJStreamConfig.init()
    KYJStreamLogger.init()
    KYJStreamConfig.set_config(KYJStreamInit.__crypt_config_section,KYJStreamInit.__crypt_config_key,"IXqAiIIVkcD8t70E")
    print('========== KYJStream init end ==========')