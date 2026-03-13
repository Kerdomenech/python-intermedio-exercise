# asientencias del personal
clases = int(input("Ingrese la cantidad de clases asistidas en el mes: "))

# clasificacion por asistencia
if clases < 5:
    print("Asistencia baja")
elif 6 <= clases <= 8:
    print("Asistencia media")
else:
    print("Asistencia alta")