from framework_init import kyj_stream
from lib.exception.config_not_found_exception import ConfigNotFoundException 
from lib.log import KYJStreamLogger
import traceback

class ErrorHandler:

  @kyj_stream.errorhandler(Exception)
  def global_error_handler(ex):
    print(ex)
    KYJStreamLogger.log_error('caught ',ex)
    return "Exception"
