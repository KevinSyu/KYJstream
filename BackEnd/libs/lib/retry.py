from functools import wraps
from flask import request
import time

def retry(exception,times = 3,delay = 3):
  def decorator(func):
    @wraps(func)
    def retry_function(*args, **kwargs):
      for count_times in range(times):
        try:
          func(*args)
        except exception:
          if count_times+1 == times:
            raise exception
          time.sleep(delay)
          continue
    return retry_function
  return decorator