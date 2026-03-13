#menu de informacion para el cliente
print ("menu")
print ("1.cafe $4000")
print ("2.te $3500")
print ("3.jugo $5000")


#contador de bebidas
cafe = 0
te = 0
jugo = 0

#utilizacion de condicional
for sab in range (0,5,1):
    bebida = int(input ("¿cual bebida prefieres? 1 o 2 o 3\n")) 
    if ( bebida== 1): 
        cafe+= 1 
    elif ( bebida==2): 
        te+=1 
    elif ( bebida==3): 
        jugo+=1
        
#valores por cantidades e items del menu       
print (f"cantidad de cafe ={cafe}")
print (f"total a unidad ={cafe*4000}")
print (f"cantidad de te ={te}")
print (f"total a unidad ={te*3500}")
print (f"cantidad de jugo={jugo}")
print (f"total a unidad ={jugo*5000}")

#valor total de todos los items selecionados
total = cafe*4000+te*3500+jugo*5000
print(f"total a pagar = ", total)