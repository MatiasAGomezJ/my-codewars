def conversor_dict_to_string(d):

    assert isinstance(d, dict)

    string = ""

    for item in d:
        string += str(item) + d[item]

    return string

def encoder(data):

    assert isinstance(data, str)

    solucion = ""

    strings = { 0 : ''} 

    contador_palbras_diferentes = 1
    acumulador = ""
    for char in data:
        acumulador += char
        if acumulador not in strings.values():
            strings[contador_palbras_diferentes] = acumulador
            solucion += "0" + str(acumulador[len(acumulador)-1])
            acumulador = ""
            contador_palbras_diferentes += 1

    solution = conversor_dict_to_string(strings)

    return solucion


if __name__ == '__main__':
    assert encoder('ABAABABAABAB') == '0A0B1A2A4A4B'
    assert encoder('ABAABABAABAB') == '0A0B1A2A4A4B'
    assert encoder('ABAABABAABABAA') == '0A0B1A2A4A4B3'
    assert encoder('ABBCBCABABCAABCAABBCAA') == '0A0B2C3A2A4A6B6'
    assert encoder('AAAAAAAAAAAAAAA') == '0A1A2A3A4A'
    assert encoder('ABCABCABCABCABCABC') == '0A0B0C1B3A2C4C7A6'
    assert encoder('ABCDDEFGABCDEDBBDEAAEDAEDCDABC') == '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C'