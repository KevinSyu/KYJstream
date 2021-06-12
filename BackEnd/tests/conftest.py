import pytest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from framework_init import FrameWork

from lib.init import KYJStreamInit
from lib.db_manager import DBManager

@pytest.fixture
def client():
    KYJStreamInit.init()
    DBManager.init()

    clean_db()

    app = FrameWork.create_app()
    test_client = app.test_client()
    yield test_client
    test_client.delete()
  
def clean_db():
  db = DBManager.get_db()
  db.get_connection()

  tables = db.execute_sql_with_transaction("show tables").fetchall() # ex. [('alembic_version',), ('room_info',), ('user_info',)]

  for table in tables:
    if table[0] == "alembic_version":
      continue
    db.execute_sql_with_transaction("truncate {}".format(table[0]))
  db.commit()
    

    