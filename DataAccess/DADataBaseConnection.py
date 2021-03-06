from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml

class DADataBaseConnection(object):
    __instance = None

    # Singleton Class
    def __new__(self):
        if DADataBaseConnection.__instance is None:
            DADataBaseConnection.__instance = object.__new__(self)
        DADataBaseConnection.__instance.val = repr(self)
        return DADataBaseConnection.__instance

    def __init__(self):
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            self.Name = cfg['DatabaseName']
            engine = create_engine(self.Name, echo=True) 
            session = sessionmaker(bind=engine)
            self.Session = session()

        



