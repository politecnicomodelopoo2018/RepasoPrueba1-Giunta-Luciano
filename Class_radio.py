class Radio(object):
    def __init__(self):
        self.programas = []


    def AgregarPrograma(self, programa):
        self.programas.append(programa)


    def ListadoProgramaDia(self, dia):
        ListaProgramaDia = []
        for item in self.programas:
            for item2 in item.horarios:
                if item2.dia == dia:
                    ListaProgramaDia.append(item.nombre)
        return ListaProgramaDia


