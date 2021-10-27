def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    if array1 == [] and array2 != [] or array2 == [] and array1 != []:
        return False
    
    array_pequena = array1[:]
    array_grande = array2[:]

    for numero in array_pequena:
        indice_numero = array_pequena.index(numero)
        array_pequena[indice_numero] = abs(array_pequena[indice_numero])  
    
    array_pequena.sort()
    array_grande.sort()

    cantidad_elementos = len(array_pequena)

    i = 0
    while (i < cantidad_elementos):
        if array_grande[i] != array_pequena[i]**2:
            return False

        i += 1
    
    return True

if __name__ == '__main__':
    a1 = [-121, -144, 19, -161, 19, -144, 19, -11]
    a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    assert comp(a1,a2) == True

