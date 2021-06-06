from repository.register_repo import RegisterRepo
from lib.util import generate_user_id
from lib.crypt import encrypt
from lib.exception.sql_exception import SqlException
from lib.log import KYJStreamLogger
from flask_jwt_extended import create_access_token,create_refresh_token
from vo.register_vo import RegisterVO
class RegisterService:

  def __init__(self):
    self.register_repository = RegisterRepo()

  def register_user(self,user_email,user_password):
    
    self.check_email_exist(user_email)
    
    user_id = generate_user_id()
    
    self.register_repository.create_user(user_id,user_email,encrypt(user_password),user_email)

    access_token = create_access_token(user_id)
    refresh_token = create_refresh_token(user_id)


    return  RegisterVO(access_token,refresh_token)

  def check_email_exist(self,user_email):
    
    result = self.register_repository.check_email_exist(user_email)
    
    if len(result):
      
      # KYJStreamLogger.log_error('user_email is already exist . user_email:{}'.format(user_email))
      raise SqlException('user_email is already exist')
    
    return
