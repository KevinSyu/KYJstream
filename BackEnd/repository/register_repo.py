from lib.db_manager import DBManager
from lib.db import DataBase

class RegisterRepo:
  def __init__(self):
    self.db:DataBase = DBManager.get_db()