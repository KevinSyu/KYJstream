from lib.db_manager import DBManager
from lib.db import DataBase

class TestRepo:

  TEST_SQL = "SELECT * FROM user_info"
  TEST_INSERT_SQL = 'INSERT INTO user_info (user_id, user_name, user_email, user_password, user_image, create_time_stamp, update_time_stamp) values(:user_id, :user_name, :user_email, :user_password, :user_image, now(), now())'

  def __init__(self):
    self.db:DataBase = DBManager.get_db()

  def get_test_data_from_db(self):
    self.db.get_connection()
    result = self.db.execute_sql_with_connection(self.TEST_SQL).fetchall()
    print(list(result))

  def insert_test_data_to_db(self):
    params = {
      'user_id':'1',
      'user_name':'Kevin', 
      'user_password':'PWD',
      'user_email':'Kevin@gmail.com', 
      'user_image':None
    }
    self.db.get_connection()
    self.db.execute_sql_with_transaction(self.TEST_INSERT_SQL,params) 
    self.db.commit()   
    