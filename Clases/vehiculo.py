class Vehiculo():
    ruedas = 4
    def __init__(self,año,modelo):
        self.__año = año      
        self._modelo = modelo

    def setAño(self, año):
        self.__año = año

    def getAño(self):
        return self.__año