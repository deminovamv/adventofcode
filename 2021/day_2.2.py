horizontal_position = 0
depth = 0
aim = 0
with open("input_day2.txt", "r", encoding="utf-8") as f:
    for line in f:
        command, value = line.split()
        if command == "forward":
            horizontal_position += int(value)
            if aim != 0:
                depth += aim * int(value)
        elif command == "down":
            aim += int(value)
        else:
            aim -= int(value)

print(horizontal_position * depth)
