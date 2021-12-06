from collections import defaultdict, Counter

with open("input_day6.txt", "r", encoding="utf-8") as f:
    start_fishes = list(map(int, f.read().split(',')))
    start_fishes = Counter(start_fishes)
print(start_fishes)
def solve(S, n):
    X = S
    for _ in range(n):
        Y = defaultdict(int)
        for x,cnt in X.items():
            if x==0:
                Y[6] += cnt
                Y[8] += cnt
            else:
                Y[x-1] += cnt
        X = Y
    return sum(X.values())

print(solve(start_fishes, 80))
print(solve(start_fishes, 256))

