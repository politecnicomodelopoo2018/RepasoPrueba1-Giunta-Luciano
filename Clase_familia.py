from Clase_persona import Persona
class Familia(object):
    PromedioCalorias = None
    def __init__(self):
        self.miembros = []

    def AgregarFamiliar(self, familiar):
        self.miembros.append(familiar)

    def PromedioCaloriasFamilia(self):
        sumacaloriastodos = 0
        for item in self.miembros:
            sumacaloriastodos += item.PromedioComidas()
        return sumacaloriastodos

    def QuienComioMas(self):
        maxcalorias = 0
        for item in self.miembros:
            if maxcalorias < item.PromedioComidas():
                maxcalorias = item.PromedioComidas()

        return maxcalorias

     def QuienComioMenos(self,maxcalorias):
         mincalorias = maxcalorias
         persona = None
         for item in self.miembros:
             if mincalorias > item.PromedioComidas():
                 persona = item.nombre
                 mincalorias = item.PromedioComidas()

         return persona



