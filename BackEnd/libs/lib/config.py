import configparser
import lib.exception.config_not_found_exception


class KYJStreamConfig:

    __config = configparser.ConfigParser()
    __path = "./etc/default.ini"

    @staticmethod
    def init():
        KYJStreamConfig.__config.read(KYJStreamConfig.__path)

    @staticmethod
    def get_str(section, key):
        if KYJStreamConfig.is_exist(section):
            return str(KYJStreamConfig.__config[section][key])
        raise Exception

    @staticmethod
    def is_exist(section):
        if KYJStreamConfig.__config.has_section(section):
            return True
        return False
