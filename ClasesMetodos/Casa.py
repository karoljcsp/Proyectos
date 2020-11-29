class casa:
    pisos = 2
    habitaciones = [4, 3, 2]
    baños = [5, 4, 3]
    cocina = 'Integral'
    precio = 230000000
    vendida = False
    caracteristicas_lugar = ['colegios', 'supermercados', 'zona_segura', 'transporte público', 'parqueadero privado']
    def funcion(self):
        self.vendida = True
    def estado(self):
        if (self.vendida):
            return "La casa ya fue vendida"
        else:
            return "La casa no ha sido vendida"
hogar = casa()
print("Habitaciones: ", hogar.habitaciones[1], "\t Baños: ", hogar.baños[2], "\t Concina: ", hogar.cocina)
print("Características de la zona: ", hogar.caracteristicas_lugar[0:3])
print("Precio de venta: ", hogar.precio)
hogar.funcion()
print(hogar.estado())
print("----------------------------------------------------------------------------------")

hogar2 = casa()
print("Habitaciones: ", hogar2.habitaciones[0], "\t Baños: ", hogar2.baños[1], "\t Concina: ", hogar2.cocina)
print("Características de la zona: ", hogar2.caracteristicas_lugar)
print("Precio de venta: ", hogar2.precio)
print(hogar2.estado())

