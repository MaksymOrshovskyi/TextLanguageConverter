English_letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
                   "x", "c", "v", "b", "n", "m", "[", "]", ";", "'", ",", ".", "/", "?"]

Ukranian_letters = ["й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "ф", "і", "в", "а", "п", "р", "о", "л", "д", "я",
                    "ч", "с", "м", "и", "т", "ь", "х", "ї", "ж", "є", "б", "ю", ".", ","]

string = input("Input text: ").lower()

letter = string[0]

if letter in English_letters:
    letter_mapping = dict(zip(English_letters, Ukranian_letters))
    result = ''.join([letter_mapping.get(letter, letter) for letter in string])
else:
    letter_mapping = dict(zip(Ukranian_letters, English_letters))
    result = ''.join([letter_mapping.get(letter, letter) for letter in string])

print("Result:", result)
