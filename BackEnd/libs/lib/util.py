import random
import string
import uuid
from flask import request
from lib.exception.request_format_exception import RequestFormatException

def generate_user_id():
  # first_str = ''.join(random.choice(string.ascii_letters) for i in range(7))
  # last_str = ''.join(random.choice(string.ascii_letters) for i in range(7))
  # user_email_str = user_email.split('@')[0]
  # return '{}_{}_{}'.format(first_str,user_email_str,last_str)
  return uuid.uuid4().hex

def get_json_request_body(input_request:request):
  try:
    return input_request.get_json()
  except Exception as ex:
    raise RequestFormatException('Input request format wrong')
