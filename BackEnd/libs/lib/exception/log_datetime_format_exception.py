class LogDatetimeFormatException(Exception):
  def __init__(self):
    self.message = "The format of the log datetime is wrong (it should be like 20210425T185613)"
    super().__init__()