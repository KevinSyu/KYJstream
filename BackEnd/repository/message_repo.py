from lib.db_manager import DBManager
from lib.mongodb import MongoDB
import time,datetime

class MessageRepo:

  def __init__(self):
    self.db:MongoDB = DBManager.get_mongodb()
  
  def insert_message(self, user_id, room_id, message,user_name):
    data = {
      "user_id":user_id,
      "message":message,
      "user_name":user_name,
      "insert_time":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }
    collection = self.db.get_collection('chat_room')
    collection.update({"room_id":room_id},{"$push":{"message_list":data}},upsert=True)

   