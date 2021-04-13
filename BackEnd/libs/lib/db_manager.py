from lib.config import KYJStreamConfig
from lib.db import DataBase
from sqlalchemy import create_engine
import os

class DBManager:
  
  __db_config_section = 'kyjstream.db.mysql.config'
  __db = None
  
  @staticmethod
  def init():

    DBManager.__db = DataBase(KYJStreamConfig.get_db_config_section())

  @staticmethod
  def get_db():
    return DBManager.__db


  




