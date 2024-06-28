# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio.
import os
os.system('cls' if os.name == 'nt' else 'clear')

def comparar_numeros(a,b,c):
    suma = a+b+c
    if suma >15:
        resultado = max(a,b,c)
    elif suma<10:
        resultado = min(a,b,c)
    else:
        resultado = a+b+c - min(a,b,c) - max(a,b,c)
    return resultado
    
print(comparar_numeros(8,2,3))