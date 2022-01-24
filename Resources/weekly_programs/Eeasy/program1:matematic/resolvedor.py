import ejercicio1

resultado1 = ejercicio1.funcion(12)
resultado2 = ejercicio1.funcion(20)

calc = 100

if resultado2 == True and resultado1 == True:
    calc = calc + 0
else:
    calc = calc - 50

resultado1 = ejercicio1.funcion(11)
resultado2 = ejercicio1.funcion(5)

if resultado2 == False and resultado1 == False:
    calc = calc + 0
else:
    calc = calc - 50


if calc == 100:
    print("El programa funciona correctamente...")
else:
    print("El programa no funicona...")