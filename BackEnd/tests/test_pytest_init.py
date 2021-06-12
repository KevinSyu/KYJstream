import os
from lib.util import get_json_request_body
import json


def test_pytest_init(client):
    assert os.environ.get('ENVIRONMENT') == "dockertest"
    response = client.get('http://localhost/kyj_stream/pytest_init')
    
    assert response.data == b'OK'
    assert response.status_code == 200
