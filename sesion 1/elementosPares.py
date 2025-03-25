'''
Dada una lista de elementos (array), crear una funcion que retorne una nueva lista con solo los elementos que aparecen una cantidad pares de veces.
Ejemplo:
["A","B","A","C","C","C","C"] // -> ["A","C"]
[1,2,3,1,2] // -> [1,2]
'''
def verificaDuplicados(array, elemento) -> bool:
    for i in range(len(array)):
        if elemento == array[i]:
            return False
    return True

def elementosPares(array) -> list:
    arrayElementosPares = []
    for i in range(len(array)):
        elemento = array[i]
        cantidadRepetidas = array.count(elemento)
        if (cantidadRepetidas % 2) == 0:
            if verificaDuplicados(arrayElementosPares, elemento):
                arrayElementosPares.append(elemento)
    return arrayElementosPares

#miArray = [1, 2, 3, 1, 2]
miArrayChars = ["A", "B", "A", "C", "C", "C", "C"]
#print(miArray)
print(miArrayChars)
miArrayPares = elementosPares(miArrayChars)
print(miArrayPares)

