def print_down_stars(num):
    global input_number
    current_index = num
    current_needed = current_index - 1
    space_needed = input_number - current_needed
    print((" " * space_needed) + ("* " * current_needed))


def print_stars(num):
    global input_number
    current_index = num
    current_needed = current_index + 1
    space_needed = input_number - current_needed
    print((" " * space_needed) + ("* " * current_needed))


def get_number(n):
    number = n
    for i in range(number):
        print_stars(i)
    if number > 1:
        for x in range(number, -1, -1):
            print_down_stars(x)


input_number = int(input())

get_number(input_number)
