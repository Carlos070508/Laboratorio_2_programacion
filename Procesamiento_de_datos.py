print("Registro de accesos de usuarios ")

# Lista para guardar los registros
registros = []

# Diccionario para contar accesos por usuario
contador_accesos = {}



# FUNCION PARA VALIDAR HORAS

def pedir_hora(mensaje):
    while True:
        hora = input(mensaje)

        # Debe tener exactamente 4 dígitos
        if len(hora) != 4 or not hora.isdigit():
            print(" Error: La hora debe tener 4 dígitos (HHMM). Intente de nuevo.")
            continue

        hh = int(hora[:2])
        mm = int(hora[2:])

        # Validar horas
        if hh < 0 or hh > 23:
            print(" Error: La hora (HH) debe estar entre 00 y 23.")
            continue

        # Validar minutos
        if mm < 0 or mm > 59:
            print(" Error: Los minutos (MM) deben estar entre 00 y 59.")
            continue

        return hora  # Hora válida



# FUNCION PARA CONVERTIR A FORMATO AM/PM

def convertir_a_am_pm(hora):
    hh = int(hora[:2])
    mm = hora[2:]

    if hh == 0:
        return f"12:{mm} AM"
    elif hh < 12:
        return f"{hh:02d}:{mm} AM"
    elif hh == 12:
        return f"12:{mm} PM"
    else:
        return f"{hh - 12:02d}:{mm} PM"



#       INICIO DEL PROGRAMA

total_registros = int(input("¿Cuántos registros desea ingresar?: "))

i = 0

while i < total_registros:
    print(f"\nRegistro #{i + 1}")

    usuario = input("Nombre del usuario: ")

    # Pedir horas con validación
    hora_entrada = pedir_hora("Hora de entrada (HHMM): ")
    hora_salida = pedir_hora("Hora de salida (HHMM): ")

    entrada_f = convertir_a_am_pm(hora_entrada)
    salida_f = convertir_a_am_pm(hora_salida)

    # Guardar registro
    registros.append([usuario, entrada_f, salida_f])

    # Contabilizar accesos
    if usuario not in contador_accesos:
        contador_accesos[usuario] = 0

    contador_accesos[usuario] += 1

    i += 1



#     MOSTRAR RESULTADOS

print("\nLISTA COMPLETA DE REGISTROS")
num = 1
for r in registros:
    print(f"\nRegistro {num}")
    print(f"Usuario: {r[0]}")
    print(f"Hora de entrada: {r[1]}")
    print(f"Hora de salida: {r[2]}")
    num += 1



# REPORTE DE ACCESOS

print("\nREPORTE FINAL DE ACCESOS")
for usuario, accesos in contador_accesos.items():
    print(f"Usuario: {usuario} → Accesos totales: {accesos}")
