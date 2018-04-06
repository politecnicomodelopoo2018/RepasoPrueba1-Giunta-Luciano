from Clase_Datos import Datos
from Clase_plato import Plato

class Persona(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None
    def __init__(self):
        self.registros = []
        self.PlatosConsumidos = []

    def SetNombre (self, nombre):
        self.nombre = nombre

    def SetApellido (self, apellido):
        self.apellido = apellido

    def SetFechaNac (self, fecha_nac):
        self.fecha_nacimiento = fecha_nac

    def AgregarRegistro (self, registro):
        self.registros.append(registro)

    def PromedioAnualAltura (self, año):

        promaltura = 0
        contador = 0
        for item in self.registros:
            if item.fecha.year == año:
                promaltura = promaltura + item.altura
                contador += 1
        return promaltura/contador

    def PromedioAnualPeso(self, año):
        prompeso = 0
        contador = 0
        for item in self.registros:
            if item.fecha.year == año:
                prompeso = prompeso + item.peso
                contador += 1
        return prompeso/contador

    def DiferenciaEntreañosAltura(self, añoAnterior, añoPosterior):
        promedioAlturaAnterior = self.PromedioAnualAltura(añoAnterior)
        promedioAlturaPosterior = self.PromedioAnualAltura(añoPosterior)
        promedioEntreAños = (promedioAlturaAnterior*100)/promedioAlturaPosterior
        promedioEntreAños = 100 - promedioEntreAños
        return promedioEntreAños

    def DiferenciaEntreañosPeso(self, añoAnterior, añoPosterior):
        promedioPesoAnterior = self.PromedioAnualPeso(añoAnterior)
        promedioPesoPosterior = self.PromedioAnualPeso(añoPosterior)
        promedioEntreAños = (promedioPesoAnterior*100)/promedioPesoPosterior
        promedioEntreAños = 100 - promedioEntreAños
        return promedioEntreAños

    def IngresarNuevaComida(self, platos):
        self.PlatosConsumidos.append(platos)

    def PromedioComidas(self):
        CaloriasTotales = 0
        for item in self.PlatosConsumidos:
            CaloriasTotales += item.cantidadCalorias
        return CaloriasTotales

