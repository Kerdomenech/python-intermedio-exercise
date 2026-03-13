#mostrar mensaje de bienvenida
print (" BIENVENIDOS AL GYM" )

#condicionales para ver cual es la edad del cliente
age = int(input ("¿cual es tu edad?\n"))
if age >=0 and age <= 12:
    print("edad no permitida")
elif age >=13 and age <= 17:
    print("clase juvenil")
elif age >=18 and age <=59:
    print("clase general")
elif age >=60:
    print("clase senior")
