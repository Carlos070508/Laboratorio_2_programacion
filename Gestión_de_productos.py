def sistema_inventario(): 
    print("\n Sistema de Inventario")
    
    productos = {
        "Arroz": {"precio": 1500, "cantidad": 50},
        "Azúcar": {"precio": 2500, "cantidad": 40},
        "Aceite": {"precio": 2000, "cantidad": 25},
        "Sal": {"precio": 1000, "cantidad": 60},
        "Harina": {"precio": 1800, "cantidad": 30}
    }

    while True:
        print("\n1. Comprar producto")
        print("2. Vender producto")
        print("3. Consultar inventario")
        print("4. Salir")
        op = int(input("Seleccione una opción: "))

        #COMPRAR 
        if op == 1:
            prod = input("Producto a comprar: ")

            
            if prod not in productos:
                print(f"\nProducto '{prod}' no existe. Se agregará.")
                precio_nuevo = int(input("Ingrese el precio por unidad: $"))
                cantidad_nueva = int(input("Cantidad inicial a ingresar: "))
                
                productos[prod] = {"precio": precio_nuevo, "cantidad": cantidad_nueva}

                print(f"Producto '{prod}' agregado al inventario con éxito.\n")

            
            cant = int(input("Cantidad a comprar: "))
            
            if cant > 0:
                precio_uni = int(input("Precio por unidad de la compra: $"))
                total = precio_uni * cant

                productos[prod]["cantidad"] += cant
                productos[prod]["precio"] = precio_uni 

                print("\nFACTURA DE COMPRA")
                print(f"Producto: {prod}")
                print(f"Cantidad comprada: {cant}")
                print(f"Precio por unidad: ${precio_uni}")
                print(f"TOTAL COMPRA: ${total}")
            else:
                print("Cantidad inválida.")

        # VENDER
        elif op == 2:
            prod = input("Producto a vender: ")

            if prod in productos:
                cant = int(input("Cantidad a vender: "))

                if 0 < cant <= productos[prod]["cantidad"]:
                    precio_uni = productos[prod]["precio"]
                    total = precio_uni * cant

                    productos[prod]["cantidad"] -= cant

                    print("\nFACTURA DE VENTA")
                    print(f"Producto: {prod}")
                    print(f"Cantidad vendida: {cant}")
                    print(f"Precio por unidad: ${precio_uni}")
                    print(f"TOTAL VENTA: ${total}")

                else:
                    print("Stock insuficiente o cantidad inválida.")
            else:
                print("Producto no existe.")

        # INVENTARIO
        elif op == 3:
            print("\nInventario Actual")
            for p, datos in productos.items():
                print(f"{p}: {datos['cantidad']} unidades — Precio: ${datos['precio']}")

        # SALIR
        elif op == 4:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

sistema_inventario()
