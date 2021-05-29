from flask import request
from framework_init import kyj_stream
from service.test_service import TestService
from flask_jwt_extended import create_access_token, jwt_required,create_refresh_token,get_jwt,get_jwt_header
from lib.json_response import *
from lib.validator import Validator
from lib.exception.validation_exception import ValidationException
from lib.util import get_json_request_body
from service.register_service import RegisterService
from lib.exception.register_exception import RegisterException
from vo.register_vo import RegisterVO
import json,dataclasses
  
class RegisterController:
  
  @kyj_stream.route('/register',methods=['POST'])
  @jwt_required(locations='headers',optional=True)
  def register_controller():

    request_jwt = get_jwt()
    if request_jwt:
      raise RegisterException('you are already login')

    request_body = get_json_request_body(request)

    user_email = request_body.get('user_email')
    Validator.check_user_email_validation(user_email)

    user_password = request_body.get('user_password')
    Validator.check_user_password_validation(user_password)

    user_password_confirm = request_body.get('user_password_confirm')
    if user_password != user_password_confirm:
      raise ValidationException('user_password is not equal to user_password_comfirm')

    register_service = RegisterService()

    response = register_service.register_user(user_email,user_password)    

    return api_success(response.__dict__)

  @kyj_stream.route('/refresh',methods=['POST'])
  @jwt_required(locations='headers',refresh=True)
  def get_access_token_by_refresh_token():
    aaa = get_jwt()
    print(str(aaa))
    return 'fresh'

  