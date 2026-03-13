# Variables iniciales
total_dinero = 0

# Contadores para cada servicio
corte = 0
cepillado = 0
tintura = 0

# Ciclo para los 7 clientes
for i in range(0,7,1):
    print("Registro de Atención")
    nombre = input("Nombre del cliente: ")
    print("Servicios: corte, cepillado, tintura")
    servicio = input("Servicio solicitado: ")
    valor = int(input("Valor pagado: "))
    

    total_dinero = total_dinero + valor
    
    #  tipo de servicio
    if servicio == "corte":
        corte = corte + 1
    elif servicio == "cepillado":
        cepillado = cepillado + 1
    elif servicio == "tintura":
        tintura = tintura + 1

#cuál es el servicio más solicitado
mas_solicitado = ""

if corte > cepillado and corte > tintura:
    mas_solicitado = "Corte"
elif cepillado > corte and cepillado > tintura:
    mas_solicitado = "Cepillado"
else:
    mas_solicitado = "Tintura"

# Resultados finales

print("REPORTE DEL DÍA")
print("Total recaudado: ", total_dinero)
print("Cantidad de Cortes:", corte)
print("Cantidad de Cepillados:", cepillado)
print("Cantidad de Tinturas:", tintura)
print("El servicio más pedido fue:", mas_solicitado)
