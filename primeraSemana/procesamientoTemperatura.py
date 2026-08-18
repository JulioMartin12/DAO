def promedioTemperaturas(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

todas_las_temperaturas = []
dias_bajo_cero = [] 
dias_calidos = []
dia_muy_caluroso = False

print("Bienvenido al programa de procesamiento de temperaturas\n")

for i in range(5):
    temperatura = int(input(f"Ingrese la temperatura del día {i+1} (-20 a 49): "))
    while temperatura < -20 or temperatura > 49:
        temperatura = int(input("Ingrese un valor correcto de temperatura, entre -20 y 49: "))
        
    todas_las_temperaturas.append(temperatura)
    
    if temperatura < 0:
        dias_bajo_cero.append(temperatura)
    if temperatura > 20:
        dias_calidos.append(temperatura)
    if temperatura > 40:
        dia_muy_caluroso = True

promedio_general = promedioTemperaturas(todas_las_temperaturas)

cant_dias_menores_promedio = sum(1 for t in todas_las_temperaturas if t < promedio_general)

print("\n" + "="*30)
print("La cantidad de días con temperaturas bajo cero es:", len(dias_bajo_cero))
print("Promedio de temperaturas ingresadas:", round(promedio_general, 2))
print("Promedio de temperaturas de los días cálidos:", round(promedioTemperaturas(dias_calidos), 2))
print(f"Hubo algún día muy caluroso (temperatura mayor a 40 grados): {'Sí' if dia_muy_caluroso else 'No'}")
print("La cantidad de días con temperaturas menores al promedio es:", cant_dias_menores_promedio)