# Python:

  ## 安裝環境
    Python的部分 請先下載Python 3.9.2版本
    下載完之後 請至CMD下指令: python --version
    如果有問題 請設定環境變數

    版本確認無誤，打開vsCode的Terminal，進入Backend資料夾
    請下指令:pip install -r requirements.txt
    再進入libs資料夾，下指令:pip install ./

    所有的套件都安裝成功

  ## 啟動方法:
    打開vsCode的Terminal，進入Backend資料夾
    下指令:python main.py
    在瀏覽器輸入網址:http://127.0.0.1:8888/kyj_stream/
    即可看到Hello World


  ## 存取DB:
    連線資訊都放在etc/common.ini檔裡面，請根據自己DB的設定來做修改
    存取DB的方法分2種:
    首先要先引用: from lib.db import DataBase
    接著宣告 db:DataBase = DBManager.get_db()
  ### 第一種 一般查詢:  
    data = db.execute_sql_with_connection('SELECT * FROM customers').fetchall()

  ### 第二種 交易:
    db.execute_sql_with_transaction('INSERT INTO customers (C_Id, Name,  Address, Phone)\
                              VALUES (":C_ID",":Name",  ":Address", ":Phone");',{'C_ID':90,'Name':"李3","Address":"ZZ路300號","Phone":"07-12345678"})  
    db.commit()

  * 注意!! 為防止xss 要用:xxx來插入變數

  ## log
    為記錄問題，加入了log機制，如果有需要加log，方法如下:
    首先要先引用: from lib.log import KYJStreamLogger
    接著根據你log的問題狀況來做分群，分別有error、warning、info
    log的檔案都在Backend/log目錄底下，分別有記錄過去的log以及當日的log

    * 注意!! 不要把log檔也上傳



  
  