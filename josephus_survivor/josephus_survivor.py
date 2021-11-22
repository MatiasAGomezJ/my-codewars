def josephus_survivor(cantidad_personas, num_saltos):

    lista_personas = list(range(1, cantidad_personas + 1)) # Lista en la cual se van a ir eliminando a las personas
    
    indice = 0 # El indice se utiliza para saber quien va a ser eliminado

    personas_restantes = len(lista_personas) # Creo una variable con la cantidad de items dentro de lista_personas ya que se utiliza varias veces, al principio sera igual a la cantidad_personas

    while personas_restantes > 1: # Mientras haya mas de una persona sigue

        indice += num_saltos # Se añade la cantidad de saltos desde el ultimo eliminado, al principio será desde cero

        # Si el indice esta fuera de la lista no podemos eliminar nada, por lo tanto ...
        while indice > personas_restantes:  # ... mientras el indice sea mayor a la cantidad de personas restantes ...
            indice -= personas_restantes    # ... restaremos la cantidad de personas al indice hasta que indice este en el rango

        # Lo que hago para eliminar a alguien es:
        # 1/3. Creo una lista desde la primera persona hasta la eliminada, sin contarla
        # 2/3. Creo una lista desde la persona eliminada, sin contarla, hasta la ultima persona
        # 3/3. Junto las dos listas las cuales ninguna tiene a la persona que hay que eliminar

        principio_lista = lista_personas[:indice-1]     # Creacion desde el principio de la lista hasta el eliminado
        final_lista = lista_personas[indice:]           # Creacion desde el eliminado hasta el final de la lista
        lista_personas = principio_lista + final_lista  # Junto las dos listas

        indice -= 1 # Es necesario bajar una posicion porque se tiene que empezar a contar a partir del anterior al eliminado
        
        personas_restantes = len(lista_personas) # Actualizo la cantidad de personas restantes

    return lista_personas[0] # Devuelvo la unica persona restante

if __name__ == '__main__':
    assert josephus_survivor(7, 3) == 4
    assert josephus_survivor(11, 19) == 10
    assert josephus_survivor(1, 300) == 1
    assert josephus_survivor(14, 2) == 13
    assert josephus_survivor(100, 1) == 100
