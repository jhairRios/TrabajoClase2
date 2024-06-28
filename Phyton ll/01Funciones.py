import os
os.system('cls' if os.name == 'nt' else 'clear')

#funcion con return sin argumentos

def mi_funcion():
    print("Hola mundo")
    return

mi_funcion()

resulatdo = mi_funcion()
print(resulatdo)

#funcion del factorial

def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)
    
#funcion  del factorial con for
def factorial(n):
    resulatdo = 1
    for i in range(1,n+1):
        resulatdo *= i
        return resulatdo


print (factorial(int(input("Ingrese un numero para calcular su factorial: "))))
    
#interaciones entre funciones
def funcion1():
    a=1
    return a
def funcion2(a):
    b=2+a
    return b
def funcion3(a,b):
    c=3+a+b
    return c
def funcion4(a,b,c):
    d=4+a+b+c
    return d

print(funcion4(funcion1(),funcion2(funcion1()),funcion3(funcion1(),funcion2(funcion1()))))

f1 = funcion1()
f2 = funcion2(f1)
f3 = funcion3(f1,f2)
f4 = funcion4(f1,f2,f3)
print(f4)