def how_many_odds(list_numbers):
    counter = 0
    for number in list_numbers:
        if number % 2 != 0:
            counter += 1

    return counter


print(how_many_odds([1, 2, 3, 4, 5, 6]) == 3)
print(how_many_odds([0, 2, 4, 6]) == 0)


def sum_even(list_numbers):
    even_sum = 0
    for number in list_numbers:
        if number % 2 == 0:
            even_sum += number

    return even_sum


print(sum_even([1, 2, 3, 4, 5]) == 6)
print(sum_even([0]) == 0)


def sum_negative(list_numbers):
    negative_sum = 0
    for number in list_numbers:
        if number < 0:
            negative_sum += number

    return negative_sum


print(sum_negative([1, -1, -4, 5]) == -5)


def count_words_len_5(list_words):
    word_counter = 0
    for word in list_words:
        if len(word) == 5:
            word_counter += 1

    return word_counter


print(count_words_len_5(["ciao", "hello", "ciaone", "sette"]) == 2)


def sum_number_without_first_even(list_numbers):
    even_trace = 0
    sum_result = 0
    for number in list_numbers:
        if number % 2 == 0 and even_trace == 0:
            even_trace = 1
        else:
            sum_result += number

    return sum_result


print(sum_number_without_first_even([1, 2, 3, 4, 5]) == 13)


def count_words_specific_start(list_words, start):
    word_counter = 0
    for word in list_words:
        if str(word).startswith(start):
            word_counter += 1

    return word_counter


print(count_words_specific_start(["stronzio", "stronzo", "ciao"], "str") == 2)




