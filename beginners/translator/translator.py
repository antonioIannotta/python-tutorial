vowels = ['a', 'e', 'i', 'o', 'u']


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in vowels:
            translation += "g"
        else:
            translation += letter

    return translation

print(translate("abraocedibru"))