def solution(board):
	answer = 0
	max_col = len(board[0])
	max_row = len(board)
	for i in range(1, max_row):
		for j in range(1, max_col):
			if board[i][j] == 1:
				board[i][j] = min(board[i - 1][j - 1], board[i][j - 1], board[i - 1][j]) + 1
				answer = max(answer, board[i][j])
	if answer == 0 and 1 in board[0]:
		answer = 1
	return answer ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))  # 4
print(solution([[0, 0, 0, 0], [1, 1, 1, 1]]))  # 4
