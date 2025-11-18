#Interfaz
#Solicitud de datos

#Cuadrado
def solicitar_datos_cuadrado():
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    return lado

def mostrar_area_cuadrado(area):
    print(f"El área del cuadrado es: {area}")

#Triángulo
def solicitar_datos_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return base, altura

def mostrar_area_triangulo(area):
    print(f"El área del triángulo es: {area}")

#Círculo
def solicitar_datos_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    return radio

def mostrar_area_circulo(area):
    print(f"El área del círculo es: {area}")

#Rectángulo
def solicitar_datos_rectangulo():
    base_rect = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    return base_rect, altura

def mostrar_area_rectangulo(area):
    print(f"El área del rectángulo es: {area}")

#Rombo
def solicitar_datos_rombo():
    diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
    return diagonal_mayor, diagonal_menor

def mostrar_area_rombo(area):
    print(f"El área del rombo es: {area}")

#Romboide
def solicitar_datos_romboide():
    base_romb = float(input("Ingrese la base del romboide: "))
    altura = float(input("Ingrese la altura del romboide: "))
    return base_romb, altura

def mostrar_area_romboide(area):
    print(f"El área del romboide es: {area}")

#Trapecio
def solicitar_datos_trapecio():
    base_mayor = float(input("Ingrese la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    return base_mayor, base_menor, altura

def mostrar_area_trapecio(area):
    print(f"El área del trapecio es: {area}")

#Pentágono
def solicitar_datos_pentagono():
    lado = float(input("Ingrese la longitud del lado del pentágono: "))
    apotema = float(input("Ingrese el apotema del pentágono: "))
    return lado, apotema

def mostrar_area_pentagono(area):
    print(f"El área del pentágono es: {area}")

#Menu
def mostrar_menu():
    print("\nCalculadora de Áreas de Figuras Geométricas")
    print("1. Calcular área del cuadrado")
    print("2. Calcular área del triángulo")
    print("3. Calcular área del círculo")
    print("4. Calcular área del rectángulo")
    print("5. Calcular área del rombo")
    print("6. Calcular área del romboide")
    print("7. Calcular área del trapecio")
    print("8. Calcular área del pentágono")
    print("9. Salir")
    
    opcion = int(input("Seleccione una opción (1-9): "))
    return opcion
