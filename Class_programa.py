from Class_radio import Radio
class Programa(object):
    nombre = None
    def __init__(self):

        self.horario = []
        self.conductores = []

    def SetNombre(self, nombre):
        self.nombre = nombre

    def AgregarConductor(self, conductor):
        self.conductores.append(conductor)

    def AgregarHorario(self, horario):


