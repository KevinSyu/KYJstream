from repository.register_repo import RegisterRepo

class RegisterService:

  def __init__(self):
    self.register_repository = RegisterRepo()

  def check_email_exist(self,user_email):
    
    result = self.register_repository.check_email_exist(user_email)
    
    if len(result):
      raise SqlException('user_email is already exist . user_email:{}'.format(user_email))

    return