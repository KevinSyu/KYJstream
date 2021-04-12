from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from lib.config import KYJStreamConfig
import base64 

crypt_config_section = "kyjstream.secret.crypt"
crypt_config_key = "KEY"
def encrypt(msg):
  key = bytes(KYJStreamConfig.get_str(crypt_config_section,crypt_config_key),"ascii")
  # key = bytes("IXqAiIIVkcD8t70E","ascii")
  cipher = AES.new(key,AES.MODE_ECB)

  result = base64.encodebytes(cipher.encrypt(pad(bytes(msg,"ascii"),32)))

  return result

def decrypt(msg):
  key = bytes(KYJStreamConfig.get_str(crypt_config_section,crypt_config_key),"ascii")
  # key = bytes("IXqAiIIVkcD8t70E","ascii")

  cipher = AES.new(key,AES.MODE_ECB)
  
  result = unpad(cipher.decrypt(base64.decodebytes(bytes(msg))),32)

  return result

