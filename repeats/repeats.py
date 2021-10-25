def repeats(lista):
    sumatorio = 0
    for index in lista:
        count = lista.count(index)
        if count == 1:
            sumatorio += index
    return sumatorio
    
if __name__ == '__main__':
    assert repeats([4,5,7,5,4,8]) == 15