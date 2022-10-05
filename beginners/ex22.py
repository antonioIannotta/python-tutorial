def counter_letters(word, letter_to_search):
    counter = 0
    for letter in word:
        if letter == letter_to_search:
            counter += 1

    return counter


def reverse(word):
    result = ""
    word_length = len(word) - 1
    while word_length >= 0:
        result += word[word_length]
        word_length -= 1

    return result


def mirror(word):
    return word + reverse(word)


def remove_letter(letter_to_remove, word):
    result = ""
    for letter in word:
        if not letter == letter_to_remove:
            result += letter

    return result

