max_num = 0
x = 0
y = 0
for i in range(9):
    board = list(map(int, input().split()))
    if max(board) > max_num:
        max_num = max(board)
        x = i
        y = board.index(max_num)
print(max_num)
print(x + 1, y + 1)
