#menu de informacion para el cliente
print ("menu")
print ("1.Cono $3000")
print ("2.vaso $4000")
print ("3.banana split $9000")


#contadores
cono = 0
vaso = 0
bananasplit = 0
total_ventas = 0
clientes_atendidos = 0

cli= "si"
cliente= cli

#utilizacion de controlar el ciclo

while cli == "si":
    clientes_atendidos+= 1
    print(f"registro de clientes #{clientes_atendidos}")
    helado = int(input ("¿que helado prefieres? 1 o 2 o 3\n")) 
    cantidad = int (input("¿cuantas unidades deseas?:"))
    

    #pagos

    valido=True

    if ( helado== 1): 
        cono+=cantidad
        pagoc= cantidad * 3000 
        total_ventas += pagoc
    elif ( helado==2): 
        vaso+=cantidad
        pagov= cantidad *4000 
        total_ventas += pagov
    elif ( helado==3): 
        bananasplit+=cantidad
        pagob= cantidad *9000 
        total_ventas += pagob
#otro cliente
    cli = input("\n¿Registrar otro cliente? (si/no): ")


# valores por cantidad
print("RESUMEN DE VENTAS")
print(f"Cantidad de Conos: {cono} (Total: ${cono * 3000})")
print(f"Cantidad de Vasos: {vaso} (Total: ${vaso * 4000})")
print(f"Cantidad de Banana Splits: {bananasplit} (Total: ${bananasplit * 9000})")


# pedido mas pedido
if cono >= vaso and cono >= bananasplit:
    mas_pedido = "Cono"
elif vaso >= cono and vaso >= bananasplit:
    mas_pedido = "Vaso"
else:
    mas_pedido = "Banana Split"

# Valores generales

print(f"Clientes totales atendidos: {clientes_atendidos}")
print(f"Producto más vendido: {mas_pedido}")
print(f"TOTAL GENERAL RECAUDADO: ${total_ventas}")
