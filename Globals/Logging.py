from logging import logging
import yaml


class Logger:
    def __init__(self):
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            self.FileLocation = cfg['Logging']['FileLocation']
            self.TraceLevel = cfg['Logging']['TraceLevel']
            self.logging = logging
            # TO DO tracelevel kunnen meegeven
            self.logging.basicConfig(filename = self.FileLocation,level=logging.DEBUG)

    def Debug(self,message):
        self.logging.debug(message)

    def Info(self,message):
        self.logging.info(message)

    def Warning(self,message):
        self.logging.warning(message)

x = Logger()
x.Debug('test')
