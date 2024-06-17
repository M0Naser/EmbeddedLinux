def IS_vowel(letter) :
    vowel = 'aeiouAEIOU'
    return letter in vowel

letter = 'd'
if IS_vowel(letter) :
    print(f"The letter '{letter}' is a vowel")
else :
    print(f"The letter '{letter}' isn't a vowel")