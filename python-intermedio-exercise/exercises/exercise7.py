#condicionales para ver la hora

hora = int(input ("ingresa la hora de llegada\n"))
if hora <=6 and hora <= 11:
    print("mañana")
elif hora <=12 and hora <= 17:
    print("tarde")
elif hora <=18 and hora <= 22:
    print("noche")
else:
    print("fuera del horario")
