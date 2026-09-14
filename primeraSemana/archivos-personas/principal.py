def buscar_en_archivo(apellido:str, contador:int):
    with open("primeraSemana/archivos-personas/personas.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea_limpia =linea.strip().split(",")
            contador = es_apellido(linea_limpia,apellido.upper(),contador)
        print(f'La cantidad de personas con el apellido {apellido} es de {contador}')
    
    return

def es_apellido(linea : list, apellido : str, contador: int)->int:
      if apellido in linea:
         print(f'{linea[1]} {linea[3]}') 
         contador+=1
      return contador

    

contador = 0
apellido = input("Ingrese el apellido a buscar:")

buscar_en_archivo(apellido, contador)   