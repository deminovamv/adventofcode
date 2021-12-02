horizontal_position = 0
depth = 0

with open("input_day2.txt", "r", encoding="utf-8") as f:
    for line in f:
        command, value = line.split()
        if command == "forward":
            horizontal_position += int(value)
        elif command == "down":
            depth += int(value)
        else:
            depth -= int(value)

print(horizontal_position * depth)
