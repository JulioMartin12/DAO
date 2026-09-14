def leer_archivo(lista_numero:list)->list:
    lista_numero = []
    with open("primeraSemana/archivos-numeros/numeros.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            if linea_limpia:
               lista_numero.append(int(linea_limpia))
    return lista_numero
   

lista_numeros = leer_archivo()
promedio = sum(lista_numeros)/len(lista_numeros)  
lista_mayores = list(filter(lambda numero : numero > promedio, lista_numeros))
lista_pares = list(filter(lambda numero: numero %2 == 0 , lista_numeros ))

print(f'La lista de numeros \n {lista_numeros}')    
print(f'Promedio: {promedio}')
print(f'Lista mayores al promedio cantidad {len(lista_mayores)} \n {lista_mayores} ')
print(f'Lista números pares cantidad {len(lista_pares)} \n {lista_pares} ')