'''
Mover los ceros al final
Escribir una función que tome un array de valores y retorne el mismo array pero moviendo los ceros al final.

Ejemplo:
moverCeros([false, 1, 0, 1, 2, 0, 1, 3, "a"]); // [false,1,1,2,1,3,"a",0,0]

Bonus: Implementar la función sin usar una variable de contador
'''
def moverAlFinal(array, indice) -> list:
    actual = indice
    siguiente = actual + 1
    while siguiente < len(array):
        auxiliar = array[siguiente]
        array[siguiente] = array[actual]
        array[actual] = auxiliar
        siguiente += 1
        actual += 1
    return array

def cerosAlFinal(array) -> list:
    for i in range(len(array)):
        if array[i] == 0 and array[i] is not False:
            moverAlFinal(array, i)
    return array

miArray = [False, 1, 0, 1, 2, 0, 1, 3, "a"]
print(miArray)
miArrayCerosAlFinal = cerosAlFinal(miArray)
print(miArrayCerosAlFinal)