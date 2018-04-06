from Clase_Datos import Datos
from Clase_persona import Persona
import datetime



persona = Persona()
nombre = input("Ingrese nombre de la persona: ")
apellido = input("Ingrese apellido de la persona: ")
fecha_nac = input("Ingrese fecha de nacimiento de la persona: ")

persona.SetNombre(nombre)
persona.SetApellido(apellido)
persona.SetFechaNac(fecha_nac)
contador = 0

while(1):
    registro = Datos()
    otroRegistro = "algo"
    año = int(input("Ingrese año actual: "))
    mes = int(input("Ingrese mes actual: "))
    dia = int(input("Ingrese dia actual: "))
    fecha = datetime.date(año, mes, dia)
    print(fecha)
    peso = int(input("Ingrese su peso actual: "))
    altura = int(input("Ingrese su altura actual: "))

    registro.SetPeso(peso)
    registro.SetAltura(altura)
    registro.SetFecha(fecha)

    persona.AgregarRegistro(registro)
    contador += 1

    otroRegistro = input("quiere ingresar algun otro registro?")
    if otroRegistro == "no":
        break

contadorcito = 0

for i in range(contador):
    print (str(persona.registros[contadorcito].fecha) + ", " + str(persona.registros[contadorcito].peso) + ", " + str(persona.registros[contadorcito].altura))
    contadorcito += 1

año = int(input("De que año quiere sacar su promedio?"))
promedioAltura = persona.PromedioAnualAltura(año)
promedioPeso = persona.PromedioAnualPeso(año)
print ("Peso promedio del año: " + str(promedioPeso) + " y altura promedio del año: " + str(promedioAltura))

añoanterior = int(input("Ingrese el primer año del periodo: "))
añoposterior = int(input("Ingrese el ultimo año del periodo: "))
print(str(persona.DiferenciaEntreañosAltura(añoanterior, añoposterior)) + ", " + str(persona.DiferenciaEntreañosPeso(añoanterior, añoposterior)))
