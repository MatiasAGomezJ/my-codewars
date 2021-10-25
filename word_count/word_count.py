def word_count(string):
    string.lower()
    string = string.split(' ')
    lista_definitiva = string[:]
    numero_palabras_buenas = 0
    malas_palabras = ["a", "the", "on", "at", "of", "upon", "in", "as"]
    
    rango = range(len(string))
    for indice_palabra in rango:
        for palabra_mala in malas_palabras:
            if string[indice_palabra] == palabra_mala:
                # palabra = string[indice_palabra]
                # lista_definitiva.remove(palabra)
                lista_definitiva[indice_palabra] = ''
        if string[indice_palabra].find("'") != -1 or string[indice_palabra].find("-") != -1:
            numero = 0
            numero += string[indice_palabra].count("'")
            numero += string[indice_palabra].count("-")
            numero_palabras_buenas += 1
    
    for item in lista_definitiva:
        if item 


    numero_palabras_buenas += len(lista_definitiva)

    print(lista_definitiva)
    print(numero_palabras_buenas)
    return numero_palabras_buenas

if __name__ == '__main__':
    assert word_count('hello there') == 2
    assert word_count('hello there and a hi') == 4
    assert word_count("I'd like to say goodbye") == 6
    assert word_count("Slow-moving user6463 has been here") == 6
    assert word_count("%^&abc!@# wer45tre") == 3