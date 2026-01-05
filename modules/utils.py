def find_max(number_list):
    max_number = number_list[0]
    for number in number_list:
        if number > max_number:
            max_number = number
    return max_number
