# cantidad de personas a registrar
cantidad = int(input("¿Cuántas personas desea registrar? "))

# Acumulador para el dinero
total_recaudado = 0

# Contadores 
cont_basico = 0
cont_premium = 0
cont_familiar = 0

for i in range(cantidad):
    print(" Registro ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    plan = input("Tipo de plan (basico, premium, familiar): ")
    
    # Reglas de edad
    if edad < 18:
        print("Aviso: Registro juvenil")
    elif edad >= 60:
        print("Aviso: Beneficio senior")
        
    # Asignación de precios y conteo de planes
    if plan == "basico":
        valor = 50000
        cont_basico = cont_basico + 1
    elif plan == "premium":
        valor = 90000
        cont_premium = cont_premium + 1
    elif plan == "familiar":
        valor = 130000
        cont_familiar = cont_familiar + 1
    
    #  valor  total
    total_recaudado = total_recaudado + valor

#  el plan más vendido
plan_ganador = ""
if cont_basico > cont_premium and cont_basico > cont_familiar:
    plan_ganador = "Básico"
elif cont_premium > cont_basico and cont_premium > cont_familiar:
    plan_ganador = "Premium"
else:
    plan_ganador = "Familiar"

# Reporte final

print("REPORTE DEL CLUB")
print("Total recaudado: $", total_recaudado)
print("Personas en plan Básico:", cont_basico)
print("Personas en plan Premium:", cont_premium)
print("Personas en plan Familiar:", cont_familiar)
print("El plan más vendido fue:", plan_ganador)
