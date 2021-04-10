from lib.config import KYJStreamConfig
from lib.db import DataBase
from sqlalchemy import create_engine
import os

class DBManager:
  
  __db_config_section = 'kyjstream.db.mysql.config'
  __db = None
  
  @staticmethod
  def init():
    
    if os.environ['ENVIRONMENT'] == "dockerdev":
      DBManager.__db_config_section = 'kyjstream.dockerdev.db.mysql.config'
    else:
      DBManager.__db_config_section = 'kyjstream.db.mysql.config'

    DBManager.__db = DataBase(DBManager.__db_config_section)

  @staticmethod
  def get_db():
    return DBManager.__db


  




