import re
from lib.exception.validation_exception import ValidationException
from lib.log import KYJStreamLogger

class Validator():

  email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
  password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\w._!]{8,16}$')

  def check_user_email_validation(user_email):
    if not user_email :
      raise ValidationException('user_email is None' )
      
    if Validator.email_pattern.match(user_email):
      return
    KYJStreamLogger.log_error('user_email_validation error user_email:{}'.format(user_email))
    raise ValidationException('user_email_validation error')

  def check_user_password_validation(user_password):
    if not user_password :
      raise ValidationException('user_password is None' )

    if Validator.password_pattern.match(user_password):
      return
    KYJStreamLogger.log_error('user_password_validation error user_password:{}'.format(user_password))
    raise ValidationException('user_password_validation error ')