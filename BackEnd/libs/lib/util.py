import random
import string

def generate_user_id(user_email:str):
  first_str = ''.join(random.choice(string.ascii_letters) for i in range(7))
  last_str = ''.join(random.choice(string.ascii_letters) for i in range(7))
  user_email_str = user_email.split('@')[0]
  return '{}_{}_{}'.format(first_str,user_email_str,last_str)