import random

def simulacion_sensores():
    print("\nSimulación de Red de Sensores (Temperaturas en °F)")

    sensores_verticales = int(input("Cantidad de sensores verticales: "))
    sensores_horizontales = int(input("Cantidad de sensores horizontales: "))

    t_min = float(input("Temperatura mínima posible (°F): "))
    t_max = float(input("Temperatura máxima posible (°F): "))
    
    umbral = float(input("Umbral crítico de temperatura (°F): "))

    matriz = []
    criticos = []

    for i in range(sensores_verticales):
        fila = []
        for j in range(sensores_horizontales):
            temp = round(random.uniform(t_min, t_max), 2)
            fila.append(temp)

            if temp > umbral:
                criticos.append((i, j, temp))
        matriz.append(fila)

    print("\nMatriz generada de sensores (°F):")
    for fila in matriz:
        print(fila)

    print("\nLecturas críticas (sensores que superan el umbral):")
    if len(criticos) == 0:
        print("No se detectaron temperaturas críticas.")
    else:
        for c in criticos:
            print(f"Sensor en (Vertical {c[0]}, Horizontal {c[1]}) → {c[2]} °F")

simulacion_sensores()
