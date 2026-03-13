#ropa 

#ropa_de1=20000
#ropa_de2=15000
#ropa_de3=15000
#ropa_de4=22000
#ropa_de5=250000
#ropa_de6=10000

caros=0

for deportivo in range(1, 6,1):
    precio = int(input(f"Ingresa el precio del articulo {deportivo}: "))
    if precio > 100000:
        caros = caros + 1

print(f"Productos caros: {caros}")