# acumuladores para cada categoría
total_alimento = 0
total_juguete = 0
total_accesorio = 0

print("REGISTRO DE VENTAS - TIENDA DE MASCOTAS ")

# Ciclo para pedir 10 ventas
for i in range(1, 11):
    print("Venta número:", i)
    
    # El usuario debe escribir la categoría exactamente igual: alimento, juguete o accesorio
    categoria = input("Categoría (alimento / juguete / accesorio): ")
    valor = int(input("Valor de la venta: "))
    
    # Clasificamos y acumulamos el dinero 
    if categoria == "alimento":
        total_alimento = total_alimento + valor
    elif categoria == "juguete":
        total_juguete = total_juguete + valor
    elif categoria == "accesorio":
        total_accesorio = total_accesorio + valor
    else:
        print("Error: Categoría no reconocida. El valor no se sumará.")


# Comparamos los totales entre sí
categoria_ganadora = ""
monto_maximo = 0

if total_alimento > total_juguete and total_alimento > total_accesorio:
    categoria_ganadora = "alimento"
    monto_maximo = total_alimento
elif total_juguete > total_alimento and total_juguete > total_accesorio:
    categoria_ganadora = "juguete"
    monto_maximo = total_juguete
else:
    categoria_ganadora = "accesorio"
    monto_maximo = total_accesorio

# Reporte Final

print("REPORTE DE VENTAS TOTALES")
print("Ventas de Alimento:  ", total_alimento)
print("Ventas de Juguete:   ", total_juguete)
print("Ventas de Accesorio: ", total_accesorio)
print("La categoría con más ingresos fue:", categoria_ganadora)
print("Monto total generado: ", monto_maximo)
