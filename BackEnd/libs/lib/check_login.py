from functools import wraps
from flask import request

def check_login(func):
  @wraps(func)
  def decorator(*args, **kwargs):
    print(request.get_json())
    return func(*args, **kwargs)
  return decorator