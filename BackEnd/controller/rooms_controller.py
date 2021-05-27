from flask import request
from framework_init import kyj_stream
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from lib.json_response import *
from service.room_service import RoomService
from lib.log import KYJStreamLogger
import json,dataclasses

class RoomsController:

  @kyj_stream.route('/rooms', methods=['POST'])
  # @jwt_required(locations='headers', optional=False)
  def create():
    request_body = request.get_json()

    # user_id = get_jwt_identity()
    user_id = request_body.get('user_id') # TODO:delete this line after Flask-JWT being implemented
    room_title = request_body.get('room_title')

    if user_id is None or room_title is None:
      return api_unprocessable_entity("missing params for request body")

    # TODO: 
    # check room title length after error handler was merged in sperate dev branch, else the conflicts will happened
    # (不過像這種不是critical的資料，其實交給前端檢查我覺得就夠了)

    room_service = RoomService()
    room_service.create_room(user_id, room_title)

    return api_success()