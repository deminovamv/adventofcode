with open("input_day1.txt", "r", encoding="utf-8") as f:
    input = f.read()


def solve(input):
    measurement = list(map(int, input.split()))
    count = 0
    for i in range(len(measurement) - 3):
        previous = sum(measurement[i: i + 3])
        next = sum(measurement[i + 1: i + 4])
        if next > previous:
            count += 1
    return count


print(solve(input.rstrip("\n")))
