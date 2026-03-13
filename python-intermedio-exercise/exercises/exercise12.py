# Inicializamos los contadores para las categorías
bajo_compromiso = 0
medio_compromiso = 0
alto_compromiso = 0

# Usamos un ciclo 
for i in range(1, 6,1):
    print(f" Registro de la persona {i}")
    
    #identificacion del usuario
    nombre = input("Nombre: ")
    dias = int(input("Días asistidos en la semana: "))
    minutos = int(input("Minutos promedio entrenados por día: "))

    # Clasificación usando condicionales
    if dias < 3:
        print(f"Resultado: {nombre} tiene un bajo compromiso.")
        bajo_compromiso += 1
    elif dias == 3 or dias == 4:
        print(f"Resultado: {nombre} tiene un compromiso medio.")
        medio_compromiso += 1
    else: 
        print(f"Resultado: {nombre} tiene un compromiso alto.")
        alto_compromiso += 1

#final de resultados

print("   ESTADÍSTICAS DEL GIMNASIO")

print(f"Total Bajo compromiso: {bajo_compromiso}")
print(f"Total Compromiso medio: {medio_compromiso}")
print(f"Total Compromiso alto:  {alto_compromiso}")
