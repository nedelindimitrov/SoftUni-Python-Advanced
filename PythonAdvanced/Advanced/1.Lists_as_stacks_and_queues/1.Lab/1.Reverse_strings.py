input_thing = input()
first_stack = list(input_thing)
second_stack = []

for _ in range(len(input_thing)):
    symbol_to_add = first_stack.pop()
    second_stack.append(symbol_to_add)

print("".join(second_stack))
