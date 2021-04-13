import configparser
import lib.exception.config_not_found_exception
import os

class KYJStreamConfig:

    __config = configparser.ConfigParser()

    @staticmethod
    def init():
        
        KYJStreamConfig.__config.read('./etc/default.ini')
        KYJStreamConfig.__config.read('./etc/common.ini')

        if os.environ.get('ENVIRONMENT') and os.environ.get('ENVIRONMENT') == "dockerdev":
            KYJStreamConfig.set_db_config_section('kyjstream.dockerdev.db.mysql.config')
            KYJStreamConfig.set_host('0.0.0.0')
        else:
            KYJStreamConfig.set_db_config_section('kyjstream.db.mysql.config')
            KYJStreamConfig.set_host('127.0.0.1')

        KYJStreamConfig.set_crypt_section('kyjstream.secret.crypt')
        KYJStreamConfig.set_crypt_key('KEY')
        KYJStreamConfig.set_config(KYJStreamConfig.get_crypt_section(),KYJStreamConfig.get_crypt_key(),"IXqAiIIVkcD8t70E")

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

    @staticmethod
    def get_crypt_section():
        return KYJStreamConfig.__crypt_config_section
    

    @staticmethod
    def get_crypt_key():
        return KYJStreamConfig.__crypt_config_key

    @staticmethod
    def get_db_config_section():
        return KYJStreamConfig.__db_config_section

    @staticmethod
    def get_host():
        return KYJStreamConfig.__host

    @staticmethod
    def set_crypt_section(section):
        KYJStreamConfig.__crypt_config_section = section

    @staticmethod
    def set_crypt_key(key):
        KYJStreamConfig.__crypt_config_key = key

    @staticmethod
    def set_db_config_section(section):
        KYJStreamConfig.__db_config_section = section

    @staticmethod
    def set_host(host):
        KYJStreamConfig.__host = host
