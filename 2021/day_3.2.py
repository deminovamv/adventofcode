numbers = list()
with open("input_day3.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        numbers.append(line)
width = len(numbers[0])
oxygen_generator = list(numbers)
co2_scrubber = list(numbers)
for i in range(width):
    if len(oxygen_generator) > 1:
        count_zero = len([x  for x in oxygen_generator if x[i]=='0'])
        count_one = len([x  for x in oxygen_generator if x[i]=='1'])
        if count_one >= count_zero:
            oxygen_generator = [x for x in oxygen_generator if x[i]=='1']
        else:
            oxygen_generator = [x for x in oxygen_generator if x[i]=='0']
    if len(co2_scrubber) > 1:
        count_zero = len([x  for x in co2_scrubber if x[i]=='0'])
        count_one = len([x  for x in co2_scrubber if x[i]=='1'])
        if count_one >= count_zero:
            co2_scrubber = [x for x in co2_scrubber if x[i]=='0']
        else:
            co2_scrubber = [x for x in co2_scrubber if x[i]=='1']
print(int(oxygen_generator[0],2)*int(co2_scrubber[0],2))

