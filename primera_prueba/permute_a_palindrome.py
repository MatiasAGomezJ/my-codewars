#·# Que existat solo 1 letra impar
#·# El resto de letras tienes que ser par

def permute_a_palindrome(word):
    num_total_caracteres_impares = 0
    for caracter in word:
        caracter_count = word.count(caracter)
        if caracter_count % 2 == 0:
            return True
        else:
            num_total_caracteres_impares = num_total_caracteres_impares + 1
            if num_total_caracteres_impares == 1:
                return True
            elif num_total_caracteres_impares > 1: 
                return False

if __name__ == '__main__':
    assert permute_a_palindrome('aa') == True
    assert permute_a_palindrome('baa') == True
    assert permute_a_palindrome('aab') == True
    assert permute_a_palindrome('baabcd') == False