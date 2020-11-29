from tkinter import Tk

class latinos():
    nombre= ""
    genero = ""
    edad= " "
pass
persona=latinos()
persona.nombre=str (input("Digite su nombre: "))
persona.Genero=str(input("Digite su genero: "))
persona.edad=int(input("Digite su edad: "))
print(f"Su nombre es: {persona.nombre}, Su genero es: {persona.Genero}, Su edad es: {persona.edad} años")
