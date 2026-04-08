"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    n = 10
    lista = []
    contador = 1 
    while contador <= n:
        lista.append(contador)
        contador +=1

    print("Lista genrada"+ str(n)+ ":")
    print(lista)
    


def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    if n<= 0:
        return[]

    return contar_recursividad(n - 1) + [n]
    print(contar_recursividad(20))
    
