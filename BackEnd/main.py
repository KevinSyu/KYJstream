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
from lib.crypt import encrypt
from lib.crypt import decrypt
from Crypto.Util.Padding import pad, unpad


if __name__ == "__main__":
    try:
        KYJStreamInit.init()
        DBManager.init()
        print('test git')
        FrameWork.init()


    except Exception as e:
        KYJStreamLogger.log_error(e)
        raise Exception('caught by global exception')