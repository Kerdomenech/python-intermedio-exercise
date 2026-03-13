# Variables para el total general del día
total_dia = 0
estado_cafeteria = "abierto"

print("BIENVENIDO A LA CAFETERÍA ")

# Ciclo principal: se mantiene mientras no se escriba "salir"
while estado_cafeteria != "salir":
    
    tpedido_activo = True
    while pedido_activo:
        producto = input("Producto (cafe / capuchino / pastel): ")
        
        if producto == "cafe":
            total_cliente += 4000
            print("+ Café agregado")
        elif producto == "capuchino":
            total_cliente += 7000
            print("+ Capuchino agregado")
        elif producto == "pastel":
            total_cliente += 6000
            print("+ Pastel agregado")
        elif producto == "fin" or producto == "salir":
            pedido_activo = False
            if producto == "salir":
                estado_cafeteria = "salir"
        else:
            print("(!) Producto no válido. Intenta con: cafe, capuchino o pastel.")

    #  si hubo consumo
    if total_cliente > 0:
        if total_cliente > 20000:
            # Calculamos el 10% de descuento ( //  para mantenerlo entero)
            descuento = (total_cliente * 10) // 100
            total_final = total_cliente - descuento
            print(f"¡Descuento del 10% ! (-{descuento})")
        else:
            total_final = total_cliente
            print("No aplica descuento.")

        print(f"Total a pagar por el cliente: {total_final}")
        total_dia += total_final

# Reporte de cierre

print("   CIERRE DE CAJA DEL DÍA")
print(f"Total acumulado: {total_dia}")
print("Gracias por usar el sistema.")
