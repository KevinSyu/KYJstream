from pymongo import MongoClient

from lib.config import KYJStreamConfig

class MongoDB:
  
  def __init__(self,section):
    db_url = KYJStreamConfig.get_str(section,'DB_URL')
    setting = {
      'username':KYJStreamConfig.get_str(section,'USER_NAME'),
      'password':KYJStreamConfig.get_str(section,'PASSWORD'),
      'host':KYJStreamConfig.get_str(section,'HOST'),
      'port':KYJStreamConfig.get_str(section,'PORT')
    }
    self.__db = self.__create_db(db_url.format(**setting))

  def __create_db(self,db_url):
    client = MongoClient(db_url)
    return client['kyjstream']
  
  def get_collection(self,collection):    
    return self.__db['{}'.format(collection)]