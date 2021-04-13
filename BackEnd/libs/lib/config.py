import configparser
import lib.exception.config_not_found_exception


class KYJStreamConfig:

    __config = configparser.ConfigParser()
    __default_path = "./etc/default.ini"
    __common_path = "./etc/common.ini"

    @staticmethod
    def init():
        KYJStreamConfig.__config.read(KYJStreamConfig.__default_path)
        KYJStreamConfig.__config.read(KYJStreamConfig.__common_path)

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
    
    @staticmethod
    def set_config(section,key,msg):
        if not KYJStreamConfig.is_exist(section):
            KYJStreamConfig.__config.add_section(section)
        KYJStreamConfig.__config.set(section,key,msg)
