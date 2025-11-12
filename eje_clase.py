
"""Realice un programa que sume los números impares entre el 0 y el 30 e imprima el
resultado de la suma."""


contador = 1
acumulador = 0

while contador <=30:
    if contador % 2 != 0:
        acumulador +=contador
    contador +=1
print("La suma de los numeros impares es:   ",acumulador)


"""-----------------------------------------------------------------------------------"""


"""Realice un programa que pida al usuario 10 números enteros (debe leerlos uno a
uno), y luego muestre en pantalla la suma de todos los números ingresados por el
usuario."""



contador = 0
acumulador = 0


while contador < 10:
    numeros = int (input("Ingrese un numero:    "))
    acumulador += numeros
    contador += 1
print("La suma de los numeros ingresados es:    ",acumulador)



"""----------------------------------------------------------------------------------"""


"""Realice un programa que le pida al usuario 10 nombres, y cuente cuantas veces
escribió el nombre “Juan” (valide para que cuente a Juan, sin importar los cambios
tipográficos de mayúsculas o minúsculas)."""



contador = 1
acumulador = 0


while contador <=4:
    nombre = input("Ingrese su nombre:  ").upper()
    if nombre == "JUAN":
        acumulador += 1
    contador += 1
print ("El nombre juan fue el nombre mas digitado:",acumulador,"veces")



"""-----------------------------------------------------------------------------------"""



"""¿Recuerdas el juego de apostar un dinero y que dados 3 números ganaba 3 veces lo
apostado, una vez y media, o perdía todo? Te propongo un reto, que tal si tomamos
ese juego, y lo organizamos para que el usuario al correrlo pueda jugar 5 veces y
luego de esas 5 veces le mostremos con cuánto dinero terminó."""



import random as r

dinero = int(input("Ingrese cantidad de dinero: "))
rondas = 1

while rondas <= 5:
    print(f"\n--- Ronda {rondas} ---")
    num = r.randint(0, 4)
    num2 = r.randint(0, 4)
    num3 = r.randint(0, 4)

    print("Tus números son:", num, num2, num3)

    if num == num2 == num3:
        ganancia = dinero * 3
        dinero = ganancia
        print(f" Ganaste 3 veces lo apostado. Actualmente cuentas con: {dinero}")
    elif num == num2 or num2 == num3 or num == num3:
        ganancia = dinero * 1.5
        dinero = ganancia
        print(f" Ganaste una vez y media. Actualmente cuentas con:  {dinero}")
    else:
        print("Perdiste mi león")
        dinero = 0

    rondas += 1

print("\n Suerte para la proxima")
print(f"Terminaste con {dinero} de dinero.")



"""------------------------------------------------------------------------------"""



"""Realice un programa que lea N empleados de una fábrica, y a cada uno le pida,
nombre, edad, salario, gastos mensuales.
a. Muestre cuánto suma el salario resultante (salario – gastos mensuales) de
todos empleados.
b. Indique a cuántos empleados, sus gastos superan el salario."""



n = int(input("Ingrese la cantidad de empleados: "))

cont = 1
suma = 0
gastos_mayores = 0

while cont <= n:
    print(f"\nEmpleado {cont}:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario: "))
    gastos = float(input("Gastos mensuales: "))

    resultante = salario - gastos
    suma += resultante

    if gastos > salario:
        gastos_mayores += 1

    cont += 1


print(f"La suma de los salarios resultantes es: {suma}")
print(f"Empleados con gastos mayores que su salario: {gastos_mayores}")







