from flask import request
from framework_init import kyj_stream
from service.test_service import TestService
from lib.db_manager import DBManager
from lib.db import DataBase

class TestController:

  @kyj_stream.route('/',methods=['GET'])
  def test():
    request_body = request.args.to_dict()
    test_service = TestService()
    test_service.get_test_data_from_db()

    return "Hello World"
