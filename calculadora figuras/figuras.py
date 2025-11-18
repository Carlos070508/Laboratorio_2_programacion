#Figuras
# #importar libreria
import math

#Area cuadrado
def area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el lado."""
    area = lado * lado
    return area

#Area Triangulo
def area_triangulo(base, altura):
    """Calcula el área de un triángulo dado la base y la altura."""
    area = (base * altura) / 2
    return area

#Area circulo
def area_circulo(radio):
    """Calcula el área de un círculo dado el radio."""
    area = math.pi * (radio ** 2)
    return area

#Area rectangulo
def area_rectangulo(base_rect, altura):
    """Calcula el área de un rectángulo dado la base y la altura."""
    area = base_rect * altura
    return area

# area rombo
def area_rombo(diagonal_mayor, diagonal_menor):
    """Calcula el área de un rombo dado las diagonales."""
    area = (diagonal_mayor * diagonal_menor) / 2
    return area

#area romboide
def area_romboide(base_romb, altura):
    """Calcula el área de un romboide dado la base y la altura."""
    area = base_romb * altura
    return area

#area trapecio
def area_trapecio(base_mayor, base_menor, altura):
    """Calcula el área de un trapecio dado las bases y la altura."""
    area = ((base_mayor + base_menor) / 2) * altura
    return area

# area pentagono
def area_pentagono(lado, apotema):
    """Calcula el área de un pentágono dado el lado y el apotema."""
    area = (5 * lado * apotema) / 2
    return area