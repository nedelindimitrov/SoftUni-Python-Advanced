input_string = input()

stack = []

current_index = 0

for digit in input_string:

    current = digit

    if current == "(":
        stack.append(current_index)

    if current == ")":
        this_print = input_string[stack.pop():current_index + 1]
        print(this_print)

    current_index += 1
