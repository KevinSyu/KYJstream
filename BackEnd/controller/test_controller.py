from flask import Blueprint
from framework_init import kyj_stream


class TestController:

  @kyj_stream.route('/')
  def test():
    return 'Hello World'
