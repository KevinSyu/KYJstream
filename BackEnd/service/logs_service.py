import os
from lib.config import KYJStreamConfig
from lib.log import KYJStreamLogger
from lib.file_handler import KYJFileHandler
from datetime import datetime, timedelta, date
import re
import json

class LogsService:
  __log_path_section     = 'kyjstream.config'
  __time_param_format    = '%Y%m%dT%H%M%S'
  __time_log_file_format = '%Y-%m-%d %H:%M:%S'
  __date_log_file_format = '%Y-%m-%d'

  def __init__(self, time_begin, time_end, names, levels, keywords, regex):
    self.log_path = KYJStreamConfig.get_str(self.__log_path_section, 'LOG_PATH') + KYJStreamConfig.get_str(self.__log_path_section, 'LOG_NAME')

    # prepare variable for time
    self.time_begin = None
    self.time_end = None
    if time_begin:
      self.time_begin = datetime.strptime(time_begin, self.__time_param_format)
    if time_end:
      self.time_end = datetime.strptime(time_end, self.__time_param_format)
      
    # prepare variable for filtering name
    self.name_list = []
    if names:
      name_list = names.split(",")
    
    # prepare variable for filtering level
    self.level_list = []
    if levels:
      level_list = levels.split(",")

    # prepare variable for filtering keyword
    self.keyword_and_list = []
    self.keyword_or_list = []
    if keywords:
      if "&&" in keywords:
        self.keyword_and_list = keywords.split("&&")
      elif "||" in keywords:
        self.keyword_or_list = keywords.split("||")
      else:
        self.keyword_and_list = [keywords]
    
    self.regex = regex

  def search_log_list(self):
    log_list = self.__get_log_list(self.time_begin, self.time_end)
    log_result_list = []
    
    # filter each log
    for log in log_list:
      log_time = datetime.strptime(log["time"], self.__time_log_file_format)
      if self.time_end and log_time > self.time_end:
        break
      if self.time_begin and log_time < self.time_begin:
        continue
      if not self.__is_list_match(log["name"], self.name_list):
        continue
      if not self.__is_list_match(log["level"], self.level_list):
        continue
      if not self.__is_keyword_match(log["msg"]):
        continue
      if not self.__is_regex_match(log["msg"]):
        continue
      
      # add to result if everying matches
      log_result_list.append(log)

    return log_result_list


  # all methods below are private
  def __is_keyword_match(self, msg):
    if self.keyword_and_list:
      for keyword in self.keyword_and_list:
        if not keyword in msg:
          return False

    if self.keyword_or_list:
      if not any(keyword in msg for keyword in self.keyword_or_list):
        return False
        
    return True

  def __is_regex_match(self, msg):
    if self.regex:
      return (self.regex and re.match(r"{}".format(self.regex), msg))
    return True

  def __is_list_match(self, log_item, item_list):
    if item_list:
      return any(log_item in item for item in item_list)
    return True

  def __get_log_list(self, time_begin, time_end):
    log_list = []

    # calculate date
    date_begin = datetime(2021, 3, 1).date() # the date we start to develop KYJStream
    date_end = date.today()
    if time_end:
      date_end = time_end.date()
    if time_begin:
      date_begin = time_begin.date()

    day_count = (date_end - date_begin).days + 1

    # read all log files
    lines = []
    for single_date in (date_begin + timedelta(n) for n in range(day_count)):
      log_path = self.log_path
      if not date.today() == single_date:
        log_path += ".{}".format(single_date.strftime(self.__date_log_file_format))

      if os.path.exists(log_path):
        log_file = KYJFileHandler(log_path)
        lines += log_file.readlines()

    for line in lines:
      line_split = line.split(' - ', 3)

      # check whether this line is a new log or not (by checking if line start with date)
      if re.match(r"^(\d+\D*){6}", line_split[0]):
        log_list.append({
          "time":  line_split[0].strip(),
          "name":  line_split[1].strip(),
          "level": line_split[2].strip(),
          "msg":   line_split[3].strip()
        })
      else:
        log_list[-1]["msg"] += line

    return log_list