# Punto 1
p_int = float(input('Ingrese  el interes: '))
cap = float(input('Ingrese el capital: '))
int = cap * p_int
if int > 7000:
    capf = cap + int
    print(capf);
else: print(f'No hay reinversión, intereses:  {int}')

# Punto 2
nota1 =(float(input('Ingrese la nota 1: ')))
nota2 =(float(input('Ingrese la nota 2: ')))
nota3 =(float(input('Ingrese la nota 3: ')))
promedio = (nota1 + nota2 + nota3)/3
if promedio>70:
    print(f'La materia se aprobó con un promedio de: {promedio}')
else: print(f'La materia no se aprobó con un promedio de: {promedio}')

# Punto 3
compra = float(input('Ingrese el valor de la compra: '))
if compra > 1000:
    desc = compra * 0.20
else:
    desc = 0
tot_pag = compra - desc
print(f'El total a pagar es de: {tot_pag}')

# Punto 4
num_horas_trab = int(input('Ingrese el número de horas trabajadas: '))
if num_horas_trab <= 40:
    pago = num_horas_trab * 16
elif num_horas_trab > 40:
    he = num_horas_trab - 40
    pago = (40 * 16) + (he *20)
print(f'El pago es de: {pago}')

# Punto 5
p_int = float(input('Ingrese  el interes: '))
cap = float(input('Ingrese el capital: '))
int = cap * p_int
if int > 7000:
    capf = cap + int
    print(capf);
else: print(f'No hay reinversión, intereses:  {int}')

#Punto 6
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese un número: '))
if(num1<num2):
    print(num1,', ', num2)
else:
    print(num2, ', ', num1)