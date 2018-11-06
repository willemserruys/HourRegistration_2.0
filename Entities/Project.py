from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
Base = declarative_base()


class Project(Base):
    __tablename__ = "tblProject"
    id = Column(Integer,primary_key = True,name = "PRO_ID")
    description = Column(String(50),nullable = False,name = "PRO_Description")
    externalId = Column(String(50),nullable = False,name = "PRO_ExterneID")
    active = Column(Integer,nullable = False,name = "PRO_Actief")
    
    def __repr__(self):
        return self.description