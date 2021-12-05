diagram = {}

with open("input_day5.txt", "r", encoding="utf-8") as f:
    for line in f:
        l_points, r_points = line.split(' -> ')
        x1, y1 = map(int, l_points.split(","))
        x2, y2 = map(int, r_points.split(","))
        distance_x = x2 - x1
        distance_y = y2 - y1
        if distance_x: distance_x = distance_x // abs(distance_x)
        if distance_y: distance_y = distance_y // abs(distance_y)
        x = x1
        y = y1
        while True:
            diagram[(x, y)] = diagram.get((x, y), 0) + 1
            if x == x2 and y == y2:
                break
            x += distance_x
            y += distance_y

t = 0
for v in diagram.values():
    if v > 1:
        t += 1

print(t)