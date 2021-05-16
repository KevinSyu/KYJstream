from lib.db_manager import DBManager
from lib.db import DataBase
from lib.exception.sql_exception import SqlException

class RegisterRepo:
  SQL_CHECK_EMAIL_EXIST = 'SELECT user_email FROM user_info WHERE user_email = :user_email'

  def __init__(self):
    self.db:DataBase = DBManager.get_db()

  def check_email_exist(self,user_email):
    self.db.get_connection()
    params = {
      'user_email':user_email
    }
    result = self.db.execute_sql_with_connection(self.SQL_CHECK_EMAIL_EXIST,params).fetchall()
    
    return result
    
