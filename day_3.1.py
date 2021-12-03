count_list_one = [0]*12
count_list_zero = [0]*12
gamma = [0] * 12
epsilon = [0] * 12

with open("input_day3.txt", "r", encoding="utf-8") as f:
    for number in f:
        number = list(number)
        for i in range(12):
            if number[i] == '1':
                count_list_one[i] += 1
            else:
                count_list_zero[i] +=1
for i in range(len(count_list_zero)):
    if count_list_zero[i] > count_list_one[i] :
        gamma[i] = '0'
        epsilon[i] = '1'
    else:
        gamma[i] = '1'
        epsilon[i] = '0'


print(count_list_zero,count_list_one)
print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))