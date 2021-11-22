def josephus_survivor(cantidad_personas, num_saltos):
    lista_personas = list(range(1, cantidad_personas + 1))
    
    indice = 0

    len_lista_personas = len(lista_personas)
    while len(lista_personas) > 1:  # Pongo el len(..) porque si no tengo que actualizar la variable cada ciclo

        indice += num_saltos

        if indice > len_lista_personas:
            indice -= len_lista_personas

        principio_lista = lista_personas[:indice-1]
        final_lista = lista_personas[indice:]
        lista_personas = principio_lista + final_lista
        indice -= 1




    return

if __name__ == '__main__':
    assert josephus_survivor(7, 3) == 4
    assert josephus_survivor(11, 19) == 10
    assert josephus_survivor(1, 300) == 1
    assert josephus_survivor(14, 2) == 13
    assert josephus_survivor(100, 1) == 100
