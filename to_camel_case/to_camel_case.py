def to_camel_case(string):
    if string == '':
        return ''
    
    string_list = string.split ('-')
    string = ' '.join(string_list)
    string_list = string.split ('_')
    string = ' '.join(string_list)
    string_list = string.split (' ')
    string = ''.join(string_list)

    rango = range(len(string_list))
    for indice in rango:
        if string_list[indice] == string_list[0]:
            continue
        string_list[indice] = string_list[indice].title()

    lista_junta = ''.join(string_list)

    return lista_junta


if __name__ == '__main__':
    assert to_camel_case('') == ''
    assert to_camel_case("The-Stealth_Warrior") == "TheStealthWarrior"
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"