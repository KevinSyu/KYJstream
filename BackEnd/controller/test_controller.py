from flask import request
from framework_init import kyj_stream
from service.test_service import TestService
from lib.db_manager import DBManager
from lib.db import DataBase
from lib.retry import retry
from lib.check_login import check_login
from functools import wraps
from lib.exception.config_not_found_exception import ConfigNotFoundException
from flask_jwt_extended import create_access_token, jwt_required
  
class TestController:
  
  @kyj_stream.route('/',methods=['GET'])
  # @check_login
  def test():
    # request_body = request.args.to_dict()
    # test_service = TestService()
    # test_service.get_test_data_from_db()
    # print(request.args.to_dict())
    # TestController.print_test('TEST Retry')
    access_token = create_access_token('123456')
    return access_token

  @kyj_stream.route('/',methods=['POST'])
  @jwt_required(locations='headers')
  def test2():
    return 'OK'

  @retry(exception=ConfigNotFoundException,times=2, delay=0)
  def print_test(msg):
    raise ConfigNotFoundException('config not found')