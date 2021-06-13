from repository.room_repo import RoomRepo
import uuid

class RoomService:

  def __init__(self):
    self.room_repo = RoomRepo()

  def create_room(self, user_id, room_title):
    #TODO: make the column to be 36 long, or make uuid str(uuid.uuid4()).replace("-", "") to a helper method
    room_id = str(uuid.uuid4()).replace("-", "") 
    self.room_repo.create_room(user_id, room_id, room_title)

    return