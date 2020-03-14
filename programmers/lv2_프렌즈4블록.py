# 각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다


def remove(board, h, w):
    tmp_count = 0
    count = 0
    new_board = [[''] * w for x in range(h)]
    check_board = [[0] * w for x in range(h)]

    for i in range(h - 1):
        for j in range(w - 1):
            if board[i][j] != '' and (board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]):
                check_board[i][j] = 1
                check_board[i + 1][j] = 1
                check_board[i][j + 1] = 1
                check_board[i + 1][j + 1] = 1
                tmp_count += 1

    if tmp_count == 0:
        return count, new_board

    for j in range(w):
        idx = h - 1
        for i in range(h - 1, -1, -1):
            if check_board[i][j] == 1:
                count += 1
            else:
                new_board[idx][j] = board[i][j]
                idx -= 1
    return count, new_board


def solution(m, n, board):
    answer = 0
    while True:
        i, new_board = remove(board, m, n)
        if i == 0:
            break
        else:
            answer += i
            board = new_board
    return answer


print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))  # 14
print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))  # 15
