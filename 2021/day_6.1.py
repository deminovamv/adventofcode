with open("input_day6.txt", "r", encoding="utf-8") as f:
    start_fishes = list(map(int, f.read().split(',')))
# print(start_fishes)
for day in range(80):
    for ind in range(len(start_fishes)):
        if start_fishes[ind] == 0:
            start_fishes[ind] = 6
            start_fishes.append(8)
        else:
            start_fishes[ind] -= 1
print(len(start_fishes))