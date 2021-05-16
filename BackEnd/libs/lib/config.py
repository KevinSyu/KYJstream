import configparser
import lib.exception.config_not_found_exception
import os

class KYJStreamConfig:

    __config = configparser.ConfigParser()
    __host_section = 'kyjstream.env.config'
    __host_key = 'HOST_KEY'

    @staticmethod
    def init():
        
        KYJStreamConfig.__config.read('./etc/default.ini')
        KYJStreamConfig.__config.read('./etc/common.ini')

        if  os.environ.get('ENVIRONMENT') == "dockerdev":
            KYJStreamConfig.__config.read('./etc/common_docker_dev.ini')
        else:
            KYJStreamConfig.__config.read('./etc/common_local_dev.ini')

        KYJStreamConfig.set_crypt_section('kyjstream.secret.crypt')
        KYJStreamConfig.set_crypt_key('KEY')
        KYJStreamConfig.set_config(KYJStreamConfig.get_crypt_section(),KYJStreamConfig.get_crypt_key(),"IXqAiIIVkcD8t70E")

    @staticmethod
    def get_str(section, key):
        if KYJStreamConfig.is_exist(section):
            return str(KYJStreamConfig.__config[section][key])
        raise Exception
    
    @staticmethod
    def get_int(section, key):
        if KYJStreamConfig.is_exist(section):
            return int(KYJStreamConfig.__config[section][key])
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
    def get_host():        
        return KYJStreamConfig.get_str(KYJStreamConfig.__host_section,KYJStreamConfig.__host_key)

    @staticmethod
    def set_crypt_section(section):
        KYJStreamConfig.__crypt_config_section = section

    @staticmethod
    def set_crypt_key(key):
        KYJStreamConfig.__crypt_config_key = key
