from framework_init import kyj_stream
from lib.exception.config_not_found_exception import ConfigNotFoundException 
from lib.exception.datetime_format_exception import DatetimeFormatException
from lib.exception.validation_exception import ValidationException 
from lib.log import KYJStreamLogger
import traceback
import flask_jwt_extended.exceptions
from jwt.exceptions import *
from flask_jwt_extended.exceptions import *
from lib.json_response import *

class ErrorHandler:

  @kyj_stream.errorhandler(DatetimeFormatException)
  def datetime_format_error_handler(ex):
    KYJStreamLogger.log_error(str(ex),ex)
    return api_unprocessable_entity(str(ex))
  
  @kyj_stream.errorhandler(ValidationException)
  def validation_error_handler(ex):
    KYJStreamLogger.log_error(str(ex),ex)
    return api_unprocessable_entity(str(ex))

  @kyj_stream.errorhandler(ExpiredSignatureError)
  def jwt_token_error_handler(ex):
    KYJStreamLogger.log_error(str(ex),ex)
    return api_unprocessable_entity(str(ex))

  @kyj_stream.errorhandler(JWTExtendedException)
  def flask_jwt_token_error_handler(ex):
    KYJStreamLogger.log_error(str(ex),ex)
    return api_unprocessable_entity(str(ex))    

  @kyj_stream.errorhandler(PyJWTError)
  def jwt_token_error_handler(ex):
    KYJStreamLogger.log_error(str(ex),ex)
    return api_unprocessable_entity(str(ex))    
    
  @kyj_stream.errorhandler(Exception)
  def global_error_handler(ex):
    KYJStreamLogger.log_error('caught ',ex)
    return "Exception"


