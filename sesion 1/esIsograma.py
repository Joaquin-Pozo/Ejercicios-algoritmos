'''
Un isograma es una palabra que no tiene letras repetidas. Consideraciones Adicionales:

    Un string vacío es un isograma.
    La función tiene que ser case insensitive e ignorar acentos.
    Si el string tiene mas de una palabra retornar false.
    Se tiene que hacer clean up del string antes de comparar.

Ejemplos:
func("Murciélago"); // returns true
func("reto"); // returns false
func("Casa"); // returns false
func("PeRrO"); // returns false
func("GaTo"); // returns true
'''
def esIsograma(palabra):
    if len(palabra) == 0:
        return False
    else:
        for i in range(len(palabra)):
            for j in range(i + 1, len(palabra)):
                #print("El caracter: " + palabra[i] + " es comparado con: " + palabra[j])
                if palabra[i].casefold() == palabra[j].casefold():
                    return False
        return True 
    

palabra = "GaTo"
if (esIsograma(palabra)):
    print("La palabra " + palabra + " es un isograma")
else:
    print("La palabra " + palabra + " no es un isograma")