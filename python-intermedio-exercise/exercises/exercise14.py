# Pedimos la capacidad inicial de la sala
capacidad_total = int(input("Ingrese la capacidad total de la sala de cine: "))

# Inicializamos los contadores para las categorías y el total
ninos = 0
adultos = 0
adultos_mayores = 0
total_ingresados = 0

print(f"Iniciando registro para {capacidad_total} personas...")

# El ciclo 
for i in range(1, capacidad_total + 1):
    print(f"Persona {i} de {capacidad_total}")
    
    edad = int(input(f"Ingrese la edad de la persona: "))
    
    # Clasificación por edad usando condicionales
    if edad < 13:
        print("Clasificación: Niño")
        ninos += 1
    elif 13 <= edad < 60:
        print("Clasificación: Adulto")
        adultos += 1
    else:
        # 60 años o más
        print("Clasificación: Adulto mayor")
        adultos_mayores += 1
    
    
    total_ingresados += 1

# Reporte final

print("REPORTE DE OCUPACIÓN")

print(f"Total de personas registradas: {total_ingresados}")
print(f"Niños: {ninos}")
print(f"Adultos: {adultos}")
print(f"Adultos mayores: {adultos_mayores}")

# Verificación de sala llena

if total_ingresados == capacidad_total:
    print("Estado de la sala: ¡LLENA!")
else:
    print("Estado de la sala: Hay asientos disponibles.")