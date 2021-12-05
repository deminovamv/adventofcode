diagram = {}
with open("input_day5.txt", "r", encoding="utf-8") as f:
    for line in f:
        l_points, r_points = line.split(' -> ')
        x1, y1 = map(int, l_points.split(","))
        x2, y2 = map(int, r_points.split(","))
        # print(x1,y1,x2,y2)
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    diagram[(x, y)] = diagram.get((x, y), 0) + 1
# print(diagram)
k = 0
for val in diagram.values():
    if val > 1:
        k +=1
print(k)