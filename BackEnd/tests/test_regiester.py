import os
from lib.util import get_json_request_body
import json

mimetype = 'application/json'

headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

url = 'http://localhost/kyj_stream/register'

def test_register(client):
    
    data = {
        "user_email": "pytest@gmail.com",
        "user_password": "Kyjstream123",
        "user_password_confirm": "Kyjstream123"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    response_json = json.loads(response.data)
    
    assert response_json['status'] == 'success'
    assert response_json['data']['access_token']
    assert response_json['data']['refresh_token']

def test_register_failed_by_email(client):
    data = {
        "user_email": "@gmail.com",
        "user_password": "Kyjstream123",
        "user_password_confirm": "Kyjstream123"
    }
    response = client.post(url, data=json.dumps(data), headers=headers)
    response_json = json.loads(response.data)
    
    assert response_json['status'] == 'error'
    assert response_json['message'] == 'user_email_validation error'
    assert response_json.get('data') == None