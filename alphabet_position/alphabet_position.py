import string as String

def alphabet_position(input):
    string_buena = input.lower().replace(' ', '')

    alphabet_position = ''
    for character in string_buena:
        if character not in (String.punctuation + String.digits):
            alphabet_position = alphabet_position + ' ' + str(String.ascii_lowercase.index(character) + 1)

    return alphabet_position.strip()

if __name__ == '__main__':
    assert alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    assert alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"