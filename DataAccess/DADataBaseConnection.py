from sqlalchemy import create_engine

class DADataBaseConnection(object):
    __instance = None

    # Singleton Class
    def __new__(self):
        if DADataBaseConnection.__instance is None:
            DADataBaseConnection.__instance = object.__new__(self)
        DADataBaseConnection.__instance.val = repr(self)
        return DADataBaseConnection.__instance

