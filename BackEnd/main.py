from flask import Flask
from lib.init import KYJStreamInit
from lib.config import KYJStreamConfig
from framework_init import FrameWork

if __name__ == "__main__":
    KYJStreamInit.init()
    # FrameWork.init()   
