def simulador_banco():
    print("SIMULADOR DE BANCO")

    # Cuentas iniciales
    cuentas = {
        1001: {"nombre": "Farid", "saldo": 500000},
        1002: {"nombre": "Jesús David", "saldo": 350000},
        1003: {"nombre": "Carlos", "saldo": 420000}
    }

    # La cola se maneja con una lista
    cola = []

    # se guardan todas las operaciones
    historial = []

    while True:
        # Menú principal
        print("\n1. Agregar operación a la cola")
        print("2. Procesar siguiente operación")
        print("3. Mostrar saldos actuales")
        print("4. Mostrar historial")
        print("5. Salir")

        op = input("Seleccione una opción: ")

        #Agregar operación a la cola
        if op == "1":
            print("Nueva operación (deposito / retiro / consulta)")

            tipo = input("Tipo de operación: ").lower()

            #tipo de accion
            if tipo not in ["deposito", "retiro", "consulta"]:
                print("Tipo inválido.")
                continue

            #número de cuenta
            try:
                num = int(input("Número de cuenta: "))
            except:
                print("Número inválido.")
                continue

            #existencia de la cuenta
            if num not in cuentas:
                print("La cuenta no existe.")
                continue

            #monto
            monto = 0
            if tipo in ["deposito", "retiro"]:
                try:
                    monto = float(input("Monto: "))
                    if monto <= 0:
                        print("Monto inválido.")
                        continue
                except:
                    print("Monto inválido.")
                    continue

            #operación a la cola
            cola.append((tipo, num, monto))
            print("Operación añadida a la cola.")

        #cola
        elif op == "2":
            if not cola:
                print("No hay operaciones en la cola.")
                continue

            # 
            tipo, num, monto = cola.pop(0)
            nombre = cuentas[num]["nombre"]
            saldo = cuentas[num]["saldo"]

            print(f"Procesando operación de {nombre}...")

            #DEPÓSITO
            if tipo == "deposito":
                cuentas[num]["saldo"] += monto
                final = cuentas[num]["saldo"]
                print(f"Depósito realizado. Nuevo saldo: ${final}")

                # Registrar en historial
                historial.append(f"{nombre} | Depósito | +${monto} | Saldo final: ${final}")

            #RETIRO
            elif tipo == "retiro":
                if monto > saldo:
                    print("Fondos insuficientes.")
                    historial.append(
                        f"{nombre} | Retiro FALLIDO | -${monto} | Saldo: ${saldo} (Insuficiente)"
                    )
                else:
                    cuentas[num]["saldo"] -= monto
                    final = cuentas[num]["saldo"]
                    print(f"Retiro realizado. Nuevo saldo: ${final}")

                    historial.append(f"{nombre} | Retiro | -${monto} | Saldo final: ${final}")

            #CONSULTA
            elif tipo == "consulta":
                print(f"Saldo actual de {nombre}: ${saldo}")

                historial.append(f"{nombre} | Consulta | Saldo: ${saldo}")

        # saldos
        elif op == "3":
            print("Saldos actuales:")
            for c, info in cuentas.items():
                print(f"{info['nombre']} (Cuenta {c}): ${info['saldo']}")

        # historial
        elif op == "4":
            print("Historial de operaciones:")
            if not historial:
                print("No hay operaciones registradas.")
            else:
                for h in historial:
                    print(h)

    
        #salir
        elif op == "5":
            print("Saldos finales:")
            for c, info in cuentas.items():
                print(f"{info['nombre']} (Cuenta {c}): ${info['saldo']}")
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# Ejecutar el simulador
simulador_banco()
