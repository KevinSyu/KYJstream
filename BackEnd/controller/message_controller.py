from flask_jwt_extended import create_access_token, jwt_required,create_refresh_token,get_jwt,get_jwt_header,get_jwt_identity
from lib.json_response import api_success
from lib.util import get_json_request_body
from lib.validator import Validator
from flask import request
from framework_init import kyj_stream
from service.message_service import MessagerService

class MessageController:

  @kyj_stream.route('/message/send',methods=['POST'])
  @jwt_required(locations='headers')
  def send_message_controller():

    request_body = get_json_request_body(request)

    user_id = get_jwt_identity()
    Validator.check_user_id_validation(user_id)

    room_id = request_body.get('room_id')
    Validator.check_room_id_validation(room_id)

    message = request_body.get('message')
    Validator.check_message_content_validation(message)
    print(message)
    message_service = MessagerService()
    message_service.send_message(user_id, room_id, message)

    return api_success("send message success")





