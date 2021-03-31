from flask import Flask
from lib.init import KYJStreamInit
from lib.config import KYJStreamConfig
from framework_init import FrameWork

if __name__ == "__main__":
    try:
        KYJStreamInit.init()
        FrameWork.init()   
    except Exception as e:
        print(e)