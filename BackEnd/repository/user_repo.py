from lib.db_manager import DBManager
from lib.db import DataBase
from lib.exception.sql_exception import SqlException

class UserRepo:
  SQL_CHECK_EMAIL_EXIST = 'SELECT user_email FROM user_info WHERE user_email = :user_email'
  SQL_INSERT_USER = 'INSERT user_info (user_id,user_email,user_name,user_password,create_time_stamp,update_time_stamp) values (:user_id,:user_email,:user_name,:user_password, NOW(),NOW())'
  SQL_GET_USER_NAME = 'SELECT user_name from user_info where user_id = :user_id'

  def __init__(self):
    self.db:DataBase = DBManager.get_db()

  def check_email_exist(self,user_email):
    self.db.get_connection()
    params = {
      'user_email':user_email
    }
    result = self.db.execute_sql_with_connection(self.SQL_CHECK_EMAIL_EXIST,params).fetchall()
    
    return result

  def create_user(self,user_id,user_email,user_password,user_name):
    self.db.get_connection()
    params = {
      'user_id':user_id,
      'user_email':user_email,
      'user_password':user_password,
      'user_name':user_name
    }
    try:
      self.db.execute_sql_with_transaction(self.SQL_INSERT_USER,params)
      self.db.commit()
      print(params)
    except Exception:
      self.db.rollback()
      raise SqlException('register user error')

  def get_user_name(self, user_id):
    self.db.get_connection()
    params = {
      'user_id':user_id
    }
    result = self.db.execute_sql_with_connection(self.SQL_GET_USER_NAME,params).fetchone()
    
    return result

    
    
