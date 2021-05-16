from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from lib.config import KYJStreamConfig
import base64 


PADDING = 32
ENCODE = "ascii"

def encrypt(msg):
  key = bytes(KYJStreamConfig.get_str(KYJStreamConfig.get_crypt_section(),KYJStreamConfig.get_crypt_key()),ENCODE)
  cipher = AES.new(key,AES.MODE_ECB)

  result = base64.b64encode(cipher.encrypt(pad(bytes(msg,ENCODE),PADDING)))

  return str(result)

def decrypt(msg):
  key = bytes(KYJStreamConfig.get_str(KYJStreamConfig.get_crypt_section(),KYJStreamConfig.get_crypt_key()),ENCODE)

  cipher = AES.new(key,AES.MODE_ECB)
  
  result = unpad(cipher.decrypt(base64.b64decode(msg)),PADDING)

  return str(result)

