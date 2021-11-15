def loose_change(cantidad):
    assert isinstance(cantidad, int) or isinstance(cantidad, float)
    
    monedas = {'Quarters': 25,'Dimes': 10, 'Nickels': 5, 'Pennies': 1}
    cambio = monedas.copy()
    for moneda in cambio:
        cambio[moneda] = 0
    cambio = dict.fromkeys(monedas.keys(), 0)

    cantidad_restante = cantidad
    for moneda in monedas:
        while cantidad_restante - monedas[moneda] >= 0:
            cantidad_restante -= monedas[moneda] 
            cambio[moneda] += 1
    
    return cambio

if __name__ == '__main__':
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
# Penny = 1 
# Nickel = 5
# Dime = 10
# Quarter = 25
