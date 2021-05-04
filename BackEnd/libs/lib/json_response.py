import json

# 以下是參考Jsend標準
# https://github.com/omniti-labs/jsend

def api_unprocessable_entity(message):
  return api_error(message), 422

def api_success(data = None):
  return json.dumps({
    "status": "success",
    "data" : data
  })

def api_error(message):
  return json.dumps({
    "status": "error",
    "message" : message
  })

def api_fail(failed_data = None):
  return json.dumps({
    "status" : "fail",
    "data" : failed_data
  })