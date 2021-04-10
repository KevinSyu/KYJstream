from lib.config import KYJStreamConfig
from lib.db import DataBase
from sqlalchemy import create_engine
class DBManager:
  

  __db_config_section = 'kyjstream.db.mysql.config'
  __db = None
  
  @staticmethod
  def init():
    DBManager.__db = DataBase(DBManager.__db_config_section)

  @staticmethod
  def get_db():
    return DBManager.__db


  




