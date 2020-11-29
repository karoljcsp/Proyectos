from datetime import date
from datetime import datetime

#Punto 1
# capital_invertido = (float(input('Ingrese el capital invertido: ')));
# ganancia = capital_invertido * 0.02;
# print(f"La ganancia es: {ganancia}");

#Punto 2
# sueldo_base = (float(input('Ingrese el sueldo base: ')));
# valor_venta1 = (float(input('Ingrese el primer valor: ')));
# valor_venta2 = (float(input('Ingrese el segundo valor: ')));
# valor_venta3 = (float(input('Ingrese el tercer valor: ')));
# total_ventas = valor_venta1 + valor_venta2 + valor_venta3;
# comision = total_ventas * 0.10;
# total_pago = sueldo_base + comision;
# print(f'El total del pago es: {total_pago}', f'\n la comisión es de: {comision}')
#
# #Punto 3
# total_compra =(float(input('Ingrese el total de la compra: ')))
# descuento = total_compra*0.15
# total_pago = total_compra - descuento
# print(f'El total de la compra con descuento es de: {total_pago}')
#
# #Punto 4
# nota1 =(float(input('Ingrese la nota 1: ')))
# nota2 =(float(input('Ingrese la nota 2: ')))
# nota3 =(float(input('Ingrese la nota 3: ')))
# examen_final =(float(input('Ingrese la nota del examen final: ')))
# trabajo_final =(float(input('Ingrese la nota del trabajo final: ')))
# promedio = (nota1 + nota2 + nota3)/3
# ppar = promedio * 0.55
# pef = examen_final * 0.30
# ptf = trabajo_final * 0.15
# calif_final = ppar + pef + ptf
# print(f'La calificación final es de: {calif_final}')
#
# #Punto 5
# nh = int(input('Ingrese el número de hombres: '))
# nm = int(input('Ingrese el número de mujeres: '))
# ta = nh + nm
# ph = nh*100/ta
# pm = nm*100/ta
# print(f'El porcentaje de hombres es: {ph}', f'\n El porcentaje de mujeres es: {pm}')

#Punto 6
from pip._vendor.distlib.compat import raw_input

# fnac = date(input('Ingrese su fecha de nacimiento: '))
# fecha_actual = datetime.now()
# edad = fnac - fecha_actual
# print(f'La edad es: {edad}')


'------------------------- PROBLEMAS PROPUESTOS -------------------------'
# 1
# cantidad_pesos =(float(input('Ingrese la cantidad en pesos: ')))
# valor_dolar =(float(input('Ingrese el valor del dolar: ')))
# cantidad_dolar = cantidad_pesos / valor_dolar;
# print(f'La cantidad en dolares es: {cantidad_dolar}')

#2
# numero =float(input('Ingrese un numero: '))
# valor_abs = abs(numero);
# print('El valor absoluto es: ', valor_abs)

#3
# volumen =float(input('Ingrese el volumen: '))
# presion =float(input('Ingrese la presión: '))
# temperatura =float(input('Ingrese la temperatura: '))
# masa = (presion*volumen)/(0.37*(temperatura+460))
# print(f'La masa es de: {masa}')

#4
# edad =int(input('Ingrese su edad: '))
# num_pulsaciones = (220-edad)/10
# print(f'El número de pulsaciones cada 10 segundos es de: {num_pulsaciones}')

#5
# salario =float(input('Ingrese valor del salario '))
# nuevo_salario = salario + (salario * 0.25)
# print(f'El nuevo salario es de: {nuevo_salario}')
#

#6
# presupuesto =float(input('Ingrese el presupesto: '))
# gn = presupuesto * 0.40;
# tm = presupuesto * 0.30;
# pd = presupuesto * 0.30;
# print(f'El área de Traumatología recibe: {tm}', f'\n El área de Ginecologia recibe: {gn}', f'\n El área de Pediatria recibe: {pd}')

#7
# precio_compra =float(input('Ingrese el precio del artículo: '))
# precio_venta = precio_compra + (precio_compra * 0.30)
# print(f'El precio de la venta es de: {precio_venta}')

#8
# lunes = int(input('Ingrese el tiempo del lunes: '))
# miercoles = int(input('Ingrese el tiempo del miércoles: '))
# viernes = int(input('Ingrese el tiempo del viernes: '))
# prom = (lunes + miercoles + viernes)/3
# print(f'El promedio de tiempo semanal es de: {prom} minutos')

#9
# inv1 =float(input('Ingrese la inversión de la persona 1: '))
# inv2 =float(input('Ingrese la inversión de la persona 2: '))
# inv3 =float(input('Ingrese la inversión de la persona 3: '))
# total = inv1 + inv2 + inv3;
# porc1 = inv1*100/total;
# porc2 = inv2*100/total;
# porc3 = inv3*100/total;
# print(f'El porcentaje de inversión de la persona 1 es de: {porc1},'
#       f'\n El porcentaje de inversión de la persona 2 es de: {porc2}',
#       f'\n El porcentaje de inversión de la persona 3 es de: {porc3}')

#10
ex_mat = float(input('Ingrese la nota del examen de matemáticas: ')) * 0.90
nota_tar1_mat = float(input('Ingrese la nota de la tarea 1  : '))
nota_tar2_mat = float(input('Ingrese la nota de la tarea 2: '))
nota_tar3_mat = float(input('Ingrese la nota de la tarea 3: '))
prom_tar_mat = ((nota_tar1_mat + nota_tar2_mat + nota_tar3_mat) / 3) * 0.10
prom_gen_mat = ex_mat + prom_tar_mat

ex_fis = float(input('Ingrese la nota del examen de física: ')) * 0.80
nota_tar1_fis = float(input('Ingrese la nota de la tarea 1  : '))
nota_tar2_fis = float(input('Ingrese la nota de la tarea 2: '))
prom_tar_fis = ((nota_tar1_fis + nota_tar2_fis ) / 2) * 0.20
prom_gen_fis = ex_fis + prom_tar_fis


ex_qui = float(input('Ingrese la nota del examen de química: ')) * 0.85
nota_tar1_qui = float(input('Ingrese la nota de la tarea 1  : '))
nota_tar2_qui = float(input('Ingrese la nota de la tarea 2: '))
nota_tar3_qui = float(input('Ingrese la nota de la tarea 3: '))
prom_tar_qui = ((nota_tar1_qui + nota_tar2_qui + nota_tar3_qui) / 3) * 0.15
prom_gen_qui = ex_qui + prom_tar_qui

prom_general = (prom_gen_fis + prom_gen_mat + prom_gen_qui)/3
print(f'El promedio general de matemáticas es de: {prom_gen_mat}',
      f'\n El promedio general de física es de: {prom_gen_fis}',
      f'\n El promedio general de química es de: {prom_gen_qui}',
      f'\n El promedio general en las tres materias es de: {prom_general}')
