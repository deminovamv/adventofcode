with open("input_7.txt", "r", encoding="utf-8") as f:
    horizontal_positions = list(map(int, f.read().split(",")))

q = float("inf")  # неограниченное верхнее значение

for i in range(min(horizontal_positions), max(horizontal_positions) + 1):
    t = sum(abs(x - i) for x in horizontal_positions)  # находим сумму на i шаге
    q = min(q, t)

print(q)

"""часть 2"""


def g(x):
    return x * (x + 1) // 2


q = float("inf")

for i in range(min(horizontal_positions), max(horizontal_positions) + 1):
    t = sum(g(abs(x - i)) for x in horizontal_positions)
    q = min(q, t)

print(q)
