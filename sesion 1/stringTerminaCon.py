'''
Hacer una función que reciba 2 strings (siempre los va a recibir), y devuelva si el primero termina con el segundo. Ejemplos:
func("abc", "bc"); // returns true
func("abc", "d"); // returns false
'''
def stringTerminaCon(primerString, segundoString) -> bool:
    largoSegundoString = len(segundoString)
    for i in reversed(primerString):
        while largoSegundoString > 0:
            if i == segundoString

string1 = "abc"
string2 = "bd"
print(stringTerminaCon(string1, string2))