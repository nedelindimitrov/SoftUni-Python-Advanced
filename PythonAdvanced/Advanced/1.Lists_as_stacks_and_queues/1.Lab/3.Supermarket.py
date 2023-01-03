from collections import deque

queue = deque()

while True:
    command = input()

    if command == "End":
        remaining = len(queue)
        print(f"{remaining} people remaining.")
        break

    if command == "Paid":
        for i in range(len(queue)):
            current = queue.popleft()
            print(current)
        continue

    queue.append(command)
