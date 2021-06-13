from repository.message_repo import MessageRepo
from lib.util import generate_user_id
from lib.crypt import encrypt
from lib.exception.sql_exception import SqlException
from lib.log import KYJStreamLogger
from flask_jwt_extended import create_access_token,create_refresh_token
from vo.send_message_vo import SendMessageVO
from repository.message_repo import MessageRepo
from repository.room_repo import RoomRepo
from repository.user_repo import UserRepo

class MessagerService:

  def __init__(self):
    self.message_repo = MessageRepo()
    self.user_repo = UserRepo()
    self.room_repo = RoomRepo()

  def send_message(self, user_id, room_id, message):

    self.check_room_exist(room_id)
    user_name = self.get_user_name(user_id)
    self.message_repo.insert_message(user_id, room_id, message,user_name)

    return SendMessageVO(message='send message success')

  def check_room_exist(self,room_id):
    
    result = self.room_repo.check_room_exist(room_id)
    
    if not len(result):      
      # KYJStreamLogger.log_error('room_id does not exist . room_id:{}'.format(room_id))
      raise SqlException('room_id does not exist')
    
    return

  def get_user_name(self, user_id):

    result = self.user_repo.get_user_name(user_id)

    return result[0].split('@')[0]
  
