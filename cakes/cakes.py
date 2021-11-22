def cakes(recipe, available):
    
    cantidades_posibles = 0

    #Comprobador de que en el diccionario available este todo lo de recipe
    for item in recipe:             # Por cada item en recipe
        if item not in available:   # Combprueba que no este en available
            return cantidades_posibles

    #Por cada item vamos a comprobar si tenemos la cantidad necesaria
    for item in recipe: # Por cada item en recipe
        temp_cantidad_posible = available[item] // recipe[item] # Se dividira el total guardado entre la cantidad necesaria

        if cantidades_posibles == 0:    
            cantidades_posibles = temp_cantidad_posible 

        if temp_cantidad_posible < cantidades_posibles:
            cantidades_posibles = temp_cantidad_posible

    return cantidades_posibles

if __name__ == '__main__':
    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    assert cakes(recipe, available) == 0

    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    assert cakes(recipe, available) == 2