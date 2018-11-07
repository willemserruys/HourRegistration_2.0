from DataAccess.DAProject import DAProject


class BLProject():
    def __init__(self):
        self.DA = DAProject()

    def GetById(self, Id):
        return self.DA.GetById(Id)

    def GetAll(self):
        return self.DA.GetAll()

