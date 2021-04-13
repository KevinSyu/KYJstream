from flask import Blueprint
from framework_init import kyj_stream
from lib.db_manager import DBManager
from lib.db import DataBase

class TestController:

  @kyj_stream.route('/')
  def test():
    db:DataBase = DBManager.get_db()
    data = db.execute_sql_with_connection('SELECT * FROM user_info').fetchall()

    return "Hello World"
