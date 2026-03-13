print (" BIENVENIDOS AL CINE" )

age = int(input ("¿cual es tu edad?\n"))
if age >=0 and age <= 12:
    print("Valor de boleta $8000")
elif age >=13 and age <=59:
    print("Valor de boleta $12000")
elif age >=60:
    print("Valor de boleta $9000")