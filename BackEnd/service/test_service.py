from repository.test_repo import TestRepo

class TestService:

  def __init__(self):
    self.test_repository = TestRepo()

  def get_test_data_from_db(self):
    # self.test_repository.insert_test_data_to_db()
    return self.test_repository.get_test_data_from_db()