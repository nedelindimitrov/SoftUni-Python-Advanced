from collections import deque

input_order = [int(x) for x in input().split(" ")]
input_order_deque = deque(input_order)

rack_capacity = int(input())

racks_used = 1

current_rack = 0

for _ in range(len(input_order)):
    current_dress = input_order_deque.popleft()

    if current_rack + current_dress <= rack_capacity:
        current_rack += current_dress
    else:
        racks_used += 1
        current_rack = 0
        current_rack += current_dress

print(racks_used)
