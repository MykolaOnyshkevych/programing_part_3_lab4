import re


def generate_powers(numbers, binary_length):
    list_of_powers = []
    for i in range(binary_length):
        numbers_to_bin = bin(numbers ** (i))[2:]
        if len(numbers_to_bin[i]) >= binary_length:
            break
        list_of_powers.append(numbers_to_bin)
    return list_of_powers


def find_min_number(string, pow_strings_arr: list):
    if len(string) == 0:
        return 0
    counter = 0
    for pow_string in pow_strings_arr:
        if len(pow_string) > len(string):
            continue
        result = re.match(pow_string, string)
        if result:
            index = result.end()
            inner_counter = find_min_number(string[index:], pow_strings_arr)
            if inner_counter != -1:
                if counter == 0:
                    counter = inner_counter + 1
                counter = min(counter - 1, inner_counter) + 1
    if counter == 0:
        return -1
    return counter



def count_elements_in_string(binary, numbers):
    if len(binary) > 100:
        return "please enter smaller binary number"
    elif numbers > 100:
        return "please enter smaller number"
    list_of_powers = generate_powers(numbers, len(binary))
    list_of_powers.reverse()
    return find_min_number(binary, list_of_powers)


