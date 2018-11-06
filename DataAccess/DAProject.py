from DataAccess.DADataBaseConnection import DADataBaseConnection
from Entities.Project import Project

from sqlalchemy.orm import sessionmaker

class DAProject():
    def __init__(self):
        self.dbConn = DADataBaseConnection()

    def GetAll(self):

        return self.dbConn.Session.query(Project).all()

    def GetById(self,id):
        return self.dbConn.Session.query(Project).filter(Project.id == id).all()

da = DAProject()
print(da.GetAll())
print(da.GetById(2))
