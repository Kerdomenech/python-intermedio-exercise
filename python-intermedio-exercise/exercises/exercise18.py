# Pedimos la cantidad de alumnos
cantidad = int(input("¿Cuántos estudiantes son? "))

# variables
suma_total = 0
mejor_nota = 0
mejor_nombre = ""
bajo = 0
medio = 0
alto = 0

for i in range(cantidad):
    print("Registro ")
    nombre = input("Nombre: ")
    
    speaking = int(input("Nota Speaking: "))
    listening = int(input("Nota Listening: "))
    reading = int(input("Nota Reading: "))
    
    # Promedio: sumamos las tres y dividimos entre 3
    promedio = (speaking + listening + reading) / 3
    suma_total = suma_total + promedio
    
    print("Promedio de este alumno:", promedio)
    
    # Clasificación
    if promedio < 60:
        print("Nivel: Bajo")
        bajo = bajo + 1
    elif promedio < 80:
        print("Nivel: Medio")
        medio = medio + 1
    else:
        print("Nivel: Alto")
        alto = alto + 1
        
    if promedio > mejor_nota:
        mejor_nota = promedio
        mejor_nombre = nombre

# Cálculo final del grupo
promedio_grupal = suma_total / cantidad

# Reporte final 
print("RESULTADOS DEL CURSO")
print("Promedio del grupo:", promedio_grupal)
print("El mejor fue:", mejor_nombre)
print("Nota del mejor:", mejor_nota)
print("Alumnos en Bajo:", bajo)
print("Alumnos en Medio:", medio)
print("Alumnos en Alto:", alto)