def comp(array1, array2):
    i = 0
    while (i < 2):
        if array2[i] != array1[i]**2:
            return False

        i += 1
    
    return True

if __name__ == '__main__':
    a1 = [2,3]
    a2 = [4, 9]
    assert comp(a1,a2) == True