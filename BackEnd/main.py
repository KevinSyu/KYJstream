from flask import Flask
from lib.init import KYJStreamInit
from lib.config import KYJStreamConfig
from lib.log import KYJStreamLogger
from lib.db_manager import DBManager
from framework_init import FrameWork
from lib.log import KYJStreamLogger
if __name__ == "__main__":
    try:
        KYJStreamInit.init()
        KYJStreamLogger.init()
        DBManager.init()
        
        FrameWork.init()        
    except Exception as e:
        KYJStreamLogger.log_error(e)
        print(e) 