from Clase_persona import Persona
import datetime



persona = Persona()
nombre = input("Ingrese nombre de la persona: ")
apellido = input("Ingrese apellido de la persona: ")
fecha_nac = input("Ingrese fecha de nacimiento de la persona: ")

persona.SetNombre(nombre)
persona.SetApellido(apellido)
persona.SetFechaNac(fecha_nac)
