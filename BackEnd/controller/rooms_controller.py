from flask import request
from framework_init import kyj_stream
from flask_jwt_extended import jwt_required, get_jwt_identity
from lib.json_response import *
from service.room_service import RoomService
from lib.validator import Validator
import json,dataclasses

class RoomsController:

  @kyj_stream.route('/rooms', methods=['POST'])
  @jwt_required(locations='headers', optional=False)
  def create_room():
    request_body = request.get_json()

    user_id = get_jwt_identity()
    room_title = request_body.get('room_title')

    Validator.check_room_params(user_id, room_title)

    room_service = RoomService()
    room_service.create_room(user_id, room_title)

    return api_success()