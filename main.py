from utils import count_elements_in_string
from in_out import read_numbers, write_result, input_values

if __name__ == '__main__':
    file_in = 'fantz3.in'
    file_out = "res_file.out"

    binary_number, number = read_numbers(file_in)

    result = count_elements_in_string(binary_number, number)

    write_result(file_out, result)
    print(result)



