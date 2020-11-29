#------------------NUMERO PAR-------------------#
# num1 = int(input('Ingrese el primer número: '))
# num2 = int(input('Ingrese el segundo número: '))
# if num1%2==0 and num2%2==0:
#     print('Ambos números son pares')
# elif num1%2==0 and num2%2!=0:
#     print (f'{num1} es par')
# elif num1%2!=0 and num2%2!=0:
#     print('ambos números son impares')
# elif num1%2!=0 and num2%2==0:
#     print (f'{num2} es par')

#--------------------VOCAL-------------------#
# letra = input('Ingrese una letra: ')
# if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra =='u':
#     print(f'La letra {letra} es una vocal')
# else: print(f'La letra {letra} no es una vocal')

# #------------------VOCAL---------------------#
# letra = input('Ingrese una letra: ').lower()
# if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra =='u':
#     print(f'La letra {letra} es una vocal')
# else: print(f'La letra {letra} no es una vocal')

#--------------------CALCULADORA------------------------------#
# num1= float(input("Digite un numero: "))
# num2= float(input("Digite un numero: "))
# operacion= str(input ("Digite la operación: ").upper())
# if operacion=='S':
#     suma= num1+num2
#     print(f"\n La suma es: {suma}")
# elif operacion=='R':
#     resta=num1-num2
#     print(f"\n la resta es: {resta}")
# elif operacion=='M':
#     multiplicacion=num1*num2
#     print(f"\n la multiplicación es: {multiplicacion} ")
# elif operacion== 'D':
#     division=num1/num2
#     print(f"\n la división es: {division:.2f}")
# else:
#   print("\se equivocó de operación12")

#--------------------CAJERO AUTOMÁTICO------------------------------#
saldo = 1000
print("\t.MENÜ:.")
print("1. Ingresar dinero a la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("3. Salir")
opcion= int(input("Digite una opción de menú: "))
print()#salto de linea entre las opciones
if opcion==1:
    extra=float(input("Cuánto dinero desea ingresar "))
    saldo= saldo+extra
    print(f"El dinero de la cuenta es de:{saldo}")
elif opcion==2:
    retirar = float(input("Cuánto dinero desea retirar: "))
    if retirar>saldo:
        print("Fondos insuficientes")
    else:
        saldo -= retirar
        print(f"El dinero en la cuenta es: {saldo}")
elif opcion==3:
    print(f"Dinero en la cuenta: {saldo}")
elif opcion==4:
    print("Gracias por utilizar nuestros servicios")
else:
    print("Error, se equivocó de opción" )