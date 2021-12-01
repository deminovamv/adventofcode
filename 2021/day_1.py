"""
https://adventofcode.com/2021/day/1
"""

with open("input_day1.txt", "r", encoding="utf-8") as f:
    i = 0
    count = 0
    previous = 0
    for measurement in f:
        measurement = int(measurement)
        i += 1
        if i == 1:
            continue
        elif previous < measurement:
            count += 1
        previous = measurement
print(count)
