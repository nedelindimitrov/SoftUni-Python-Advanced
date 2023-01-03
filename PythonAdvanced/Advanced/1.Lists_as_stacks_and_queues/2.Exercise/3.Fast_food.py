from collections import deque

food_we_have = int(input())

food_order_list = [int(x) for x in input().split(" ")]

print(max(food_order_list))

if food_we_have >= sum(food_order_list):
    print("Orders complete")
else:
    food_order_deque = deque(food_order_list)

    while food_we_have > 0:
        current_order = food_order_deque.popleft()
        food_we_have -= current_order
        if food_we_have < 0:
            food_order_deque.appendleft(current_order)

    final_list = list(food_order_deque)

    final_list = [str(x) for x in final_list]

    if food_we_have < sum(food_order_list):
        print(f"Orders left: " + " ".join(final_list))
