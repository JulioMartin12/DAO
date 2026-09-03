def leer_archivo():
    lista = []
    archivo = open("terceraSemana/archivo.txt")
    linea = archivo.readline()
    while linea:
        lista.append(int(linea))
        linea = archivo.readline()
    archivo.close()
    return lista


print(leer_archivo())