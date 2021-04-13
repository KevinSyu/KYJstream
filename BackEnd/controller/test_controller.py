from flask import request
from framework_init import kyj_stream
from service.test_service import TestService

class TestController:

  @kyj_stream.route('/',methods=['GET'])
  def test():
    aaa = request.args.to_dict()
    p = TestService()
    p.get_test_data_from_db()
    return 'Hello World'
