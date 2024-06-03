import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\hardi\Desktop\python\nopcommeraceApp\Configuration\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common', "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get('common', "password")
        return password
