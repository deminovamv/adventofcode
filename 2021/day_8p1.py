t = 0
with open("input_day8.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
        left, right = line.split(" | ")
        for el in right.split():
            if len(el) in [2, 3, 4, 7]:
                t += 1
print(t)