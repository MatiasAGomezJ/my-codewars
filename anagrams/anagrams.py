def anagrams(anagram, words):
    anagram_sorted = sorted(anagram) # Sort the anagram
    valid_words = []    # Create an empty array

    for word in words:  # For every word in the array word =>
        word_sorted = sorted(word) # Sort the word
        if anagram_sorted == word_sorted:   # If the sorted word is the
                                            # same as the sorted anagram =>
            valid_words.append(word)    # Then append the word to the string of valid words
    
    return valid_words # Return the array of valid words

if __name__ == '__main__':
    assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
    assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']