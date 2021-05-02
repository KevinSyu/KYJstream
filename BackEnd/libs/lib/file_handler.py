class KYJFileHandler:
  file = None

  def __init__(self, path):
    self.file = open(path)
  
  def close(self):
    self.file.close()

  def readlines(self):
    return self.file.readlines()
