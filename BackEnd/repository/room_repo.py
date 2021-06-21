from lib.db_manager import DBManager
from lib.db import DataBase
from lib.exception.sql_exception import SqlException

class RoomRepo:
  SQL_INSERT_ROOM = 'INSERT room_info (user_id, room_id, room_title, create_time_stamp, update_time_stamp) values (:user_id, :room_id, :room_title, NOW(), NOW())'
  SQL_CHECK_ROOM_EXIST = 'SELECT room_id from room_info where room_id = :room_id '
  

  def __init__(self):
    self.db:DataBase = DBManager.get_db()

  def create_room(self, user_id, room_id, room_title):
    self.db.get_connection()
    params = {
      'user_id': user_id,
      'room_id': room_id,
      'room_title': room_title,
    }
    try:
      self.db.execute_sql_with_transaction(self.SQL_INSERT_ROOM,params)
      self.db.commit()
      print(params)
    except Exception:
      self.db.rollback()
      raise SqlException('create room error')

  def check_room_exist(self, room_id):
    self.db.get_connection()
    params = {
      'room_id':room_id
    }
    result = self.db.execute_sql_with_connection(self.SQL_CHECK_ROOM_EXIST,params).fetchall()
    
    return result
