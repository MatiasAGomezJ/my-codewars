def encoder(data):
    saved_string = { 0 : ''}
    
    i = 0
    position_saved = 0
    solution = ""
    while i < len(data):
        acumulador = ''
        while acumulador in saved_string.values():
            acumulador += data[i]
            i += 1
            
        # acumulador += data[1] 
        solution += str(saved_string.keys()[saved_string.values().index(acumulador[0:-1])) + data[i-1]
        position_saved += 1
        print(solution)
        saved_string[position_saved] = acumulador

    print("pausa")
    return solution


if __name__ == '__main__':
    assert encoder('ABAABABAABAB') == '0A0B1A2A4A4B' 