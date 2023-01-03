from collections import deque

kids_string = input()
tosses_count_string = input()

kids = deque(kids_string.split(" "))
tosses_count = int(tosses_count_string)

count = 0
while len(kids) > 1:
    count += 1

    kid = kids.popleft()

    if count < tosses_count:
        kids.append(kid)
    else:
        print(f"Removed {kid}")
        count = 0

print(f"Last is {kids.pop()}")
