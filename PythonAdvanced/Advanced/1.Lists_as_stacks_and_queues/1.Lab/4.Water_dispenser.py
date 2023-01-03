from collections import deque

water_quantity = int(input())

water_queue = deque()

while True:
    command = input()

    if command == "Start":
        break

    name = command
    water_queue.append(name)

while True:
    command = input()

    if command == "End":
        print(f"{water_quantity} liters left")
        break

    if command.startswith("refill "):
        new_command = command.split(" ")
        liters = int(new_command[1])
        water_quantity += liters

    else:
        liters = int(command)

        if water_quantity >= liters:
            person = water_queue.popleft()
            print(f"{person} got water")
            water_quantity -= liters
        else:
            person = water_queue.popleft()
            print(f"{person} must wait")
