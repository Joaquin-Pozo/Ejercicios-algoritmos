/* 
Validar paréntesis
Escribe una función que tome como parametro un string con paréntesis y determina si el orden de los paréntesis es válido. 
La función debería retornar true si es válido o false si no lo es.
*/
var validarParentesis = (entrada) => {
    if (entrada.length == 1) {
        return false
    }
    if (entrada.length == 0) {
        return true
    }
    return false
}
let stringEntrada = "";
console.log(validarParentesis(stringEntrada));