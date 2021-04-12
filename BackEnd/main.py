from flask import Flask
from lib.init import KYJStreamInit
from lib.config import KYJStreamConfig
from lib.log import KYJStreamLogger
from lib.db_manager import DBManager
from framework_init import FrameWork
from lib.log import KYJStreamLogger
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64 


if __name__ == "__main__":
    try:
        KYJStreamInit.init()
        KYJStreamLogger.init()
        DBManager.init()
        key = bytes("IXqAiIIVkcD8t70E","ascii")
        cipher = AES.new(key,AES.MODE_ECB)
        s = cipher.encrypt(bytes("1234567891234567","ascii"))
        
        print(base64.encodebytes(s))
        print(base64.encodebytes(key))


        # FrameWork.init()


    except Exception as e:
        KYJStreamLogger.log_error(e)
        print(e) 