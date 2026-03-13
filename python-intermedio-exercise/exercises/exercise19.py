# Variables para contar cada categoría
agotados = 0
stock_bajo = 0
stock_normal = 0

# Ciclo para 10 productos
for i in range(10):
    print("Registro de Producto")
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad disponible: "))
    
    # Clasificación por rangos
    if cantidad == 0:
        print("Estado: Agotado")
        agotados = agotados + 1
    elif cantidad <= 5:
        print("Estado: Stock bajo")
        stock_bajo = stock_bajo + 1
    else:
        print("Estado: Stock normal")
        stock_normal = stock_normal + 1

# Reporte final
print("RESUMEN DE INVENTARIO")
print("Productos agotados:", agotados)
print("Productos con stock bajo:", stock_bajo)
print("Productos con stock normal:", stock_normal)
