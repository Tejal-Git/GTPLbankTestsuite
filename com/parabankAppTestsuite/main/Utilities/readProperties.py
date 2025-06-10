import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\Config.ini")

class Readconfig:
    @staticmethod
    def getApplicationURL():
        url=config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUserID():
        userID=config.get("common info", "UserID")
        return userID

    @staticmethod
    def getPassword():
        password=config.get("common info", "password")
        return password