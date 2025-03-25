'''
Reemplazar las letras de un string por su index en el alfabeto (e.g. A = 1 , B = 2 , C = 3 ...)
Consideraciones Adicionales:
    Ignorar espacios.
    Hacer clean up del string antes de comenzar el swap (para eliminar acentos y caracteres especiales, 
    se sugiere meter en este proceso de clean up el ignorado de espacios).
Ejemplo:
    func("abc def"); // returns '1 2 3 4 5 6';
'''
def limpiarString(stringLetras) -> list:
    arrayLetrasLimpio = []
    for char in stringLetras:
        if char != " ":
            arrayLetrasLimpio.append(char)
    return arrayLetrasLimpio

def letrasPorNumeros(stringLetras, letrasMap) -> list:
    numeros = []
    arrayLetras = limpiarString(stringLetras)
    for i in range(len(arrayLetras)):
        for j in range(len(letrasMap)):
            if arrayLetras[i] == letrasMap[j]:
                numeros.append(j + 1)
    return numeros

letrasMap = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
            "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", 
            "v", "w", "x", "y", "z"]

letras = "abc def"
numeros = letrasPorNumeros(letras, letrasMap)
print(letras)
print(numeros)