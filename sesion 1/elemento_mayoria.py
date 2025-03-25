def elemento_mayoria(array):
    largo = len(array)
    candidato = -1
    for i in range(largo - 1):
        elemento = array[i]
        contador = 1
        for j in range(i + 1, largo):
            if elemento == array[j]:
                contador += 1
            if contador > largo/2:
                candidato = elemento
    
    return candidato


my_array = [3, 3, 4, 2, 4, 4, 2, 4, 4]

resultado = elemento_mayoria(my_array)

if resultado != -1:
    print(f"Elemento de mayoría: {resultado}.")
else:
    print("No se encontró un elemento de mayoría.")

