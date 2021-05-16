from flask import request
from framework_init import kyj_stream
from service.test_service import TestService
from flask_jwt_extended import create_access_token, jwt_required,create_refresh_token,get_jwt,get_jwt_header
from lib.json_response import *
from lib.validator import Validator
from lib.exception.validation_exception import ValidationException
from service.register_service import RegisterService
  
class RegisterController:
  
  @kyj_stream.route('/login',methods=['POST'])
  @jwt_required(locations='headers',optional=True)
  def register_controller():
    jwt = get_jwt()
    print(str(jwt))

    request_body = request.get_json()

    user_email = request_body.get('user_email')
    Validator.check_user_email_validation(user_email)

    user_password = request_body.get('user_password')
    Validator.check_user_password_validation(user_password)

    user_password_confirm = request_body.get('user_password_confirm')
    if user_password != user_password_confirm:
      raise ValidationException('user_password is not equal to user_password_comfirm')

    register_service = RegisterService()

    register_service.check_email_exist(user_email)

    access_token = create_access_token(user_email)
    refresh_token = create_refresh_token(user_email)
    return api_success({'access_token':access_token,'refresh_token':refresh_token})

  @kyj_stream.route('/refresh',methods=['POST'])
  @jwt_required(locations='headers',refresh=True)
  def get_access_token_by_refresh_token():
    aaa = get_jwt()
    print(str(aaa))
    return 'fresh'

  