'''
Palindromos

Un palindromo es una palabra, frase, número o secuencia de caracteres que se lee igual al derecho o al reves.

Escribir una función que verifique si un númerospuede ser reordenado para formar un palíndromo.
Nota: Los valores siempre serán numéricos y positivos.

Ejemplo:
5        =>  true
2112     =>  true
1331     =>  true
3357665  =>  false
1294     =>  false
'''
def esPalindromo(numero) -> bool:
    if numero is not str:
        secuencia = str(numero)
    if len(secuencia) == 1 or len(secuencia) == 0:
        return True
    indiceUltimo = len(secuencia) - 1
    if secuencia[0] != secuencia[indiceUltimo]:
        return False
    return esPalindromo(secuencia[1:indiceUltimo])

secuencia = 4455665544
print(esPalindromo(secuencia))
