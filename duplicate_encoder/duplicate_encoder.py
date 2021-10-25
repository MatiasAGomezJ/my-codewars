def duplicate_encoder(word_input):
    word_input = word_input.lower()
    transformed_word = ''
    for character in word_input:
        count_character = word_input.count(character)
        if count_character > 1:
            transformed_word = transformed_word + ")"
            continue
        else:
            transformed_word = transformed_word + "("
            continue

    return transformed_word    

if __name__ == '__main__':
    assert duplicate_encoder('din') == '((('
    assert duplicate_encoder('recede')  == '()()()'
    assert duplicate_encoder('Success') == ')())())'