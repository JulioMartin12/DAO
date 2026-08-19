def menor_venta(min,min_surtidor, nuevo_valor, nuevo_numero_surtidor):
    if nuevo_valor < min:
        return nuevo_valor, nuevo_numero_surtidor
    else:
        return min, min_surtidor
    
    
total_litros = 0
menor_venta_valor = float('inf')
menor_surtidor = None
nafta_super = 0
nafta_especial = 0
gasoil = 0


print("Bienvenido a la estación de servicio\n")

for i in range(10):
    surtidor = int(input("Ingrese el número de surtidor, un valor entre 1 y 30: "))
    tipo_combustible = {1: "Nafta Super", 2: "Nafta Especial", 3: "Gasoil"}


    while surtidor < 1 or surtidor > 30 :
        surtidor = int(input("Ingrese un número correcto de surtidor, un valor entre 1 y 30: "))

    litros_surtidor = float(input("Ingrese la cantidad de litros que desea cargar: "))
    while litros_surtidor < 0:
        litros_surtidor = float(input("Ingrese un valor correcto de litros, un valor mayor a 0: "))
        
    menor_venta_valor , menor_surtidor = menor_venta(menor_venta_valor,menor_surtidor, litros_surtidor, surtidor)
    total_litros += litros_surtidor    
    tipo = int(input("Ingrese el tipo de combustible, un valor entre 1 y 3: "))
    while   int(tipo) < 1 or int(tipo) > 3:
        tipo = int(input("Ingrese un valor correcto de tipo de combustible, un valor entre 1 y 3: ")) 
    if tipo == 1:
        nafta_super += litros_surtidor
    elif tipo == 2:
        nafta_especial += litros_surtidor
    elif tipo == 3:
        gasoil += litros_surtidor
    print()    
promedio_litros = total_litros / 10
print("La cantidad total de Nafta Super es: ", nafta_super)
print("La cantidad total de Nafta Especial es: ", nafta_especial)
print("La cantidad total de Gasoil es: ", gasoil)
print("El surtidor con menor venta es el surtidor número: ", menor_surtidor, "con un total de litros cargados de: ", menor_venta_valor)
print("El promedio total de litros cargados es: ", round(promedio_litros, 2))



