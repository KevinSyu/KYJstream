from flask_jwt_extended import create_access_token, jwt_required,create_refresh_token,get_jwt,get_jwt_header
from lib.util import get_json_request_body
from flask import request

class MessageController:

  @kyj_stream.route('/message/send',methods=['POST'])
  @jwt_required(locations='headers')
  def send_message_controller():
    request_jwt = get_jwt()

    request_body = get_json_request_body(request)

    user_id = request_body.get('user_id')
    room_id = request_body.get('room_id')