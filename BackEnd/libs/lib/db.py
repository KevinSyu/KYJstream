from lib.config import KYJStreamConfig
from lib.exception.sql_exception import SqlException
from sqlalchemy import create_engine
from sqlalchemy import text

class DataBase:

  def __init__(self,section):
    db_url = KYJStreamConfig.get_str(section,'DB_URL')
    setting = {
      'username':KYJStreamConfig.get_str(section,'USER_NAME'),
      'password':KYJStreamConfig.get_str(section,'PASSWORD'),
      'host':KYJStreamConfig.get_str(section,'HOST'),
      'port':KYJStreamConfig.get_str(section,'PORT'),
      'dbname':KYJStreamConfig.get_str(section,'DB_NAME')
    }
    self.__engine = create_engine(db_url.format(**setting),pool_recycle=7200)

  def get_connection(self):
    return self.__engine.connect()

  def get_transaction(self):
    connection = self.__engine.connect()
    transaction = connection.begin()
    return transaction
  
  def execute_sql_with_connection(self,sql,params = None):
    try:
      self.connection = self.get_connection()
      if params:
        result = self.connection.execute(text(sql),params)
      else:
        result = self.connection.execute(sql)
      return result
    except Exception as e:
      raise SqlException('execute_sql_with_connection faild')
    finally:
      self.connection.close()

  def execute_sql_with_transaction(self,sql,params = None):
    try:
      self.transaction = self.get_transaction()
      if params:
        result = self.transaction.execute(text(sql),params)
      else:
        result = self.transaction.execute(sql)
      return result
    except Exception as e:
      raise SqlException('execute_sql_with_transaction faild')

  def commit(self):
    try:
      self.transaction.commit()
    except Exception as e:
      raise SqlException('commit faild')
    finally:
      self.transaction.close()
  
  def rollback(self):
    try:
      self.transaction.rollback()
    except Exception as e:
      raise SqlException('rollback faild')
    finally:
      self.transaction.close()

    