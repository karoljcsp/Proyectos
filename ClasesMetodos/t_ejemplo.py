from tkinter import *

ventana = Tk()
ventana.geometry("600x500")
ventana.title("Aplicacion")

Boton1 = Button(ventana, text="Inicio", bg="blue", fg="white")
Boton1.grid(row=8, column=1)
Boton2 = Button(ventana, text="Archivos")
Boton2.grid(row=8, column=4)
ventana.mainloop()
