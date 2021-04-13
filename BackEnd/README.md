# Python:

  ## 安裝環境
    Python的部分 請先下載Python 3.9.2版本
    下載完之後 請至CMD下指令: python --version
    如果有問題 請設定環境變數

    版本確認無誤，打開vsCode的Terminal，進入Backend資料夾
    請下指令:pip install -r requirements.txt
    再進入libs資料夾，下指令:pip install ./
    
    所有的套件都安裝成功

  ## DB Migration:
    打開terminal，需要先進入db_migrate資料夾，修改alembic.ini檔案的sqlalchemy.url，
    改為自己DB的URL，然後下指令:alembic upgrade head，會將DB結構更新至最新版本，
    如果需要回到上一版本，可下指令: alembic downgrade -1 後會數字越大 回到越前面的版本，也可以直接指定版本號
    如果需要對資料庫做DDL，則下指令:alembic revision  -m "${你要下的訊息}"，即可在./kyjAlembic/version 看到生成新的檔案
    即可寫對DB做更動的邏輯
    可參考:https://medium.com/@acer1832a/%E4%BD%BF%E7%94%A8-alembic-%E4%BE%86%E9%80%B2%E8%A1%8C%E8%B3%87%E6%96%99%E5%BA%AB%E7%89%88%E6%9C%AC%E7%AE%A1%E7%90%86-32d949f7f2c6
    做完這些即做完DB的設定

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

  ## log:
    為記錄問題，加入了log機制，如果有需要加log，方法如下:
    首先要先引用: from lib.log import KYJStreamLogger
    接著根據你log的問題狀況來做分群，分別有error、warning、info
    log的檔案都在Backend/log目錄底下，分別有記錄過去的log以及當日的log

    * 注意!! 不要把log檔也上傳

  ## 資料加解密:
    如果資料需要加密或解密，請import以下的lib
    from lib.crypt import encrypt
    from lib.crypt import decrypt
    用法:en = encrypt("想要加密的字串") OR de = decrypt("需要解密的字串")



  
  