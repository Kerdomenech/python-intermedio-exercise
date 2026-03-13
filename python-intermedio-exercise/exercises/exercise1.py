#menu de sabores
print ("menu")
print ("1.vainilla")
print ("2.chocolate")
print ("3.fresa")

#contador de sabor
sab_vainilla = 0
sab_chocolate = 0
sab_fresa = 0
#condicional 

for sab in range (0,5,1): 
    sabor = int(input ("¿cual sabor \n prefieres? 1 o 2 o 3\n")) 
    if ( sabor == 1):
        sab_vainilla+=1 
    elif ( sabor == 2): 
        sab_chocolate+=1 
    elif (sabor == 3): 
        sab_fresa+=1

#contabilizacion de cada sabor
print ("cantida de vainilla = ",sab_vainilla)
print (f"cantida de chocolate= {sab_chocolate}")
print (f"cantida de fresa= {sab_fresa}")