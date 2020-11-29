#Definición de la clase
class vehiculo:
    largochasis = 250;
    anchochasis = 120;
    ruedas = 4;
    encamino = False

    #Constructor
    def funcion(self):
        self.encamino = True

    def estado(self):
        if (self.encamino):
            return "El carro esta en marcha"
        else:
            return "El carro esta estático"
auto=vehiculo()

print("El largo de vehiculo es:", auto.largochasis)
print("El vehiculo tiene de ruedas:", auto.ruedas)

auto.funcion()
print(auto.estado())
print("----------------------------------------------------------------------------------")
auto2=auto
print("El largo de vehiculo es:", auto2.largochasis)
print("El vehiculo tiene de ruedas:",auto2.ruedas,"ruedas")
print(auto2.estado())