with open("input_day4.txt", "r", encoding="utf-8") as f:
    data = f.read()
data = data.split("\n\n")
print(data)
nums = list(map(int, data[0].split(",")))
print(nums)
boards = []
for k in data[1:]:
    boards.append([])
    for j in k.splitlines():
        boards[-1].append(list(map(int, j.split())))
print(boards[0])
for num in nums:
    # print(boards)
    for board in boards:
        for row in board:
            for i in range(len(row)):
                if row[i] == num:
                    row[i] = None
        if any(all(x == None for x in row) for row in board) \
                or any(all(row[i] == None for row in board) for i in range(len(board[0]))):
            print(sum(x or 0 for row in board for x in row) * num)
            print(board)
            print(num)
            exit(0)