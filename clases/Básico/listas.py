lista_vac=[]
print(lista_vac)

# print(lista)
# print(lista[0])
# print(lista[-1])
# print(lista[0:3])

#-------------------------------------------------------
lista1=["Lunes","Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Semana", "Mes"]
lista2=["Domingo","Festivo", "Semana", "Fin_de_Semana", "Sábado", "Martes", "Día", "Mes"]
lista_dos = [item for item in lista1 if item in lista2]
lista_primera = [item for item in lista1 if item not in lista2]
lista_segunda = [item for item in lista2 if item not in lista1]

print ('La lista uno contienen estos elementos ')
for item in lista_primera: print ('%s' % item)
print();
print ('La lista dos contienen estos elementos ')
for item in lista_segunda: print ('%s' % item)
print();
print ('Ambas lisas contienen')
for item in lista_dos: print ('%s' % item)



