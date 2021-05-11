from lib.config import KYJStreamConfig
from lib.db import DataBase
from sqlalchemy import create_engine
import os

class DBManager:
  
  __db_config_section = 'kyjstream.db.mysql.config'
  __test_db_config_section = 'kyjstream_test.db.mysql.config'
  __db = None
  __test_db = None
  
  @staticmethod
  def init():
    DBManager.__db = DataBase(DBManager.__db_config_section)

  @staticmethod
  def get_db():
    return DBManager.__db

  @staticmethod
  def init_test_db():
    DBManager.__test_db = DataBase(DBManager.__test_db_config_section)

  @staticmethod
  def get_test_db():
    return DBManager.__test_db

  




