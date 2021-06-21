from lib.config import KYJStreamConfig
from lib.db import DataBase
from lib.mongodb import MongoDB
from sqlalchemy import create_engine
import os

class DBManager:
  
  __db_config_section = 'kyjstream.db.config'
  __mongo_db_config_section = 'kyjstream.db.mongo.config'
  __test_db_config_section = 'kyjstream_test.db.config'
  __db = None
  __mongo_db = None
  __test_db = None
  
  @staticmethod
  def init():
    DBManager.__db = DataBase(DBManager.__db_config_section)
    DBManager.__mongo_db = MongoDB(DBManager.__mongo_db_config_section)
    
  @staticmethod
  def get_db():
    return DBManager.__db
  
  @staticmethod
  def get_mongodb():
    return DBManager.__mongo_db

  @staticmethod
  def init_test_db():
    DBManager.__test_db = DataBase(DBManager.__test_db_config_section)

  @staticmethod
  def get_test_db():
    return DBManager.__test_db

  




