# Variables para acumular 
total_recaudado = 0
cantidad_carros = 0
cantidad_motos = 0

# el récord del día
placa_del_que_mas_pago = ""
pago_mas_alto = 0

print("INICIO DE REGISTRO DE PARQUEADERO ")

# 3. Ciclo controlado 
for i in range(1, 9,1):
    print(" Registro del vehículo", i)
    
    placa = input("Escriba la placa: ")
    tipo = input("Escriba el tipo (carro o moto): ")
    horas = int(input("¿Cuántas horas estuvo parqueado?: "))
    
    pago_actual = 0
    
    #  Condicionales 
    if tipo == "carro":
        pago_actual = horas * 4000
        cantidad_carros = cantidad_carros + 1
    elif tipo == "moto":
        pago_actual = horas * 2000
        cantidad_motos = cantidad_motos + 1
    else:
        print("Error: El tipo escrito no es exacto. No se sumará pago.")

    # Acumular el dinero 
    total_recaudado = total_recaudado + pago_actual
    print("Monto a pagar por este vehículo:", pago_actual)

    # pago maximo
    if pago_actual > pago_mas_alto:
        pago_mas_alto = pago_actual
        placa_del_que_mas_pago = placa

# Reporte

print("REPORTE DE CIERRE")
print("Dinero total recaudado:", total_recaudado)
print("Número de carros que entraron:", cantidad_carros)
print("Número de motos que entraron:", cantidad_motos)
print("Placa del vehículo con mayor pago:", placa_del_que_mas_pago)
print("Valor de ese pago:", pago_mas_alto)