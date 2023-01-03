input_list_stack = input().split(" ")

for i in range(len(input_list_stack)):
    number = input_list_stack.pop()
    print(number, end=" ")
