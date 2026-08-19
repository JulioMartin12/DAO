import random


def simulacion():
    return None

def get_color(numero):
    
    if(numero == 0):
        return (numero, None)
    elif(numero == 10 or numero == 28):
        return (numero, "negro")
    
    suma = reducir_numero(numero)
        
    if(suma % 2 == 0):
        return (numero, "negro")
    else:
        return (numero, "rojo")
    
    

def reducir_numero(numero):
    suma= sum(int(digito) for digito  in str(numero))
    while suma > 9 :
         suma = sum(int(digito) for digito in str(suma))
    return suma


def generar_ruleta():
    ruleta = [] 
    for numero in range (0,37):
        ruleta.insert(numero,get_color(numero))
        
    return ruleta

#
# print(generar_ruleta())
ruleta = generar_ruleta()
cant_num_par = 0
cant_num_impar = 0
total_ceros = 0
cant_num_rojos = 0
cant_num_negros = 0

for numero in range(1000):
    tirada = random.randint(0,36)
    if ruleta[tirada][0] == 0:
        total_ceros += 1
    elif tirada % 2 == 0 :
        cant_num_par += 1
    else:
        cant_num_impar += 1   
    if(ruleta[tirada][1] == "rojo"):
        cant_num_rojos += 1
    elif(ruleta[tirada][1] == "negro"):
        cant_num_negros += 1


print(f'Total de pares: {cant_num_par}')
print(f'Total de impares: {cant_num_impar}')
print(f'Total de rojos: {cant_num_rojos}')
print(f'Total de negros: {cant_num_negros}')
print(f'total de promedios de ceros: {round(total_ceros/1000, 2)}')
#print(f'total de ceros: {total_ceros}')
#print(f'Total de numeros: {cant_num_par + cant_num_impar + total_ceros}')