import sys


def input_values():
    print("Input your data:")
    while True:
        values = input()
        if values == "":
            break
        binary_numbers, numbers = values.split(" ")
        binary_numbers = str(binary_numbers)
        numbers = int(numbers)

    return binary_numbers, numbers


def read_numbers(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                binary_numbers, numbers = line.split(" ")
                binary_numbers = str(binary_numbers)
                numbers = int(numbers)

            return binary_numbers, numbers

    except (FileNotFoundError):
        sys.exit(f'file "{filename}" not found')


def write_result(filename, result):
    with open(filename, "w") as file:
        file.write(str(result))
