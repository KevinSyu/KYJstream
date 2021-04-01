from flask import Flask
from lib.init import KYJStreamInit
from lib.config import KYJStreamConfig
from lib.log import KYJStreamLogger
from lib.db_manager import DBManager
from lib.db import DataBase
from framework_init import FrameWork

if __name__ == "__main__":
    try:
        KYJStreamInit.init()
        KYJStreamLogger.init()
        print('KEVIN' )
        DBManager.init()
        db:DataBase = DBManager.get_db()
        data = db.execute_sql_with_connection('SELECT * FROM KYJStream.customers').fetchall()
        # transaction目前還有問題
        # db.execute_sql_with_transaction('INSERT INTO KYJStream.test values (column_1 = :column)',{'column':99})
        # db.commit()
        print('KEVIN' + str(data))
        FrameWork.init()  
        
    except Exception as e:
       print(e) 