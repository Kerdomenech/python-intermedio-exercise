horas= int(input ("¿cuantas horas estuvo en el parqueadero? \n"))

#cuantas horas duro
if horas <=1:
    total= 5000

#calcular las horas si son mayores a 1
else :
    horas_adicionales= horas-1
    total=5000 +(horas_adicionales*3000)

print (f"total a pagar ={total}")
