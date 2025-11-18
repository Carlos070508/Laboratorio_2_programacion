
#principal
from figuras import *
from interfaz import *

#Constantes menú
CUADRADO = 1
TRIANGULO = 2
CIRCULO = 3
RECTANGULO = 4
ROMBO = 5
ROMBOIDE = 6
TRAPECIO = 7
PENTAGONO = 8
SALIR = 9

opcion = 0

while opcion != SALIR:
    opcion = mostrar_menu()

    if opcion == CUADRADO:
        lado = solicitar_datos_cuadrado()
        area = area_cuadrado(lado)
        mostrar_area_cuadrado(area)

    elif opcion == TRIANGULO:
        base, altura = solicitar_datos_triangulo()
        area = area_triangulo(base, altura)
        mostrar_area_triangulo(area)

    elif opcion == CIRCULO:
        radio = solicitar_datos_circulo()
        area = area_circulo(radio)
        mostrar_area_circulo(area)

    elif opcion == RECTANGULO:
        base_rect, altura = solicitar_datos_rectangulo()
        area = area_rectangulo(base_rect, altura)
        mostrar_area_rectangulo(area)

    elif opcion == ROMBO:
        diagonal_mayor, diagonal_menor = solicitar_datos_rombo()
        area = area_rombo(diagonal_mayor, diagonal_menor)
        mostrar_area_rombo(area)

    elif opcion == ROMBOIDE:
        base_romb, altura = solicitar_datos_romboide()
        area = area_romboide(base_romb, altura)
        mostrar_area_romboide(area)

    elif opcion == TRAPECIO:
        base_mayor, base_menor, altura = solicitar_datos_trapecio()
        area = area_trapecio(base_mayor, base_menor, altura)
        mostrar_area_trapecio(area)

    elif opcion == PENTAGONO:
        lado, apotema = solicitar_datos_pentagono()
        area = area_pentagono(lado, apotema)
        mostrar_area_pentagono(area)

    elif opcion == SALIR:
        print("\nSaliendo de la calculadora. ¡Hasta luego!\n")

    else:
        print("Opción no válida. Por favor seleccione un número del 1 al 9.")