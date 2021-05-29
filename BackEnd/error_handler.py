from framework_init import kyj_stream
from lib.exception.config_not_found_exception import ConfigNotFoundException 
from lib.exception.datetime_format_exception import DatetimeFormatException
from lib.exception.validation_exception import ValidationException 
from lib.exception.register_exception import RegisterException
from lib.exception.sql_exception import SqlException
from lib.exception.request_format_exception import RequestFormatException
from lib.log import KYJStreamLogger
import traceback
import flask_jwt_extended.exceptions
from jwt.exceptions import *
from flask_jwt_extended.exceptions import *
from lib.json_response import *

class ErrorHandler:

  @kyj_stream.errorhandler(RequestFormatException)
  def request_format_error_handler(ex):
    KYJStreamLogger.log_error(str(ex),ex)
    return api_unprocessable_entity(str(ex))

  @kyj_stream.errorhandler(DatetimeFormatException)
  def datetime_format_error_handler(ex):
    KYJStreamLogger.log_error(str(ex),ex)
    return api_unprocessable_entity(str(ex))
  
  @kyj_stream.errorhandler(ValidationException)
  def register_error_handler(ex):
    KYJStreamLogger.log_error(str(ex),ex)
    return api_unprocessable_entity(str(ex))
  
  @kyj_stream.errorhandler(RegisterException)
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

  @kyj_stream.errorhandler(SqlException)
  def sql_error_handler(ex):
    KYJStreamLogger.log_error(str(ex),ex)
    return api_unprocessable_entity(str(ex))  
    
  @kyj_stream.errorhandler(Exception)
  def global_error_handler(ex):
    KYJStreamLogger.log_error('caught ',ex)
    return "Exception"


