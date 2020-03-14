def solution(array, start, finish):
    row_max = len(array)
    col_max = len(array[0])
    visited = [[False for x in range(col_max)] for y in range(row_max)]
    max_val = move(array, row_max, col_max, start, finish, 0, visited)
    return -1 if max_val == (col_max * row_max + 1) else max_val


def move(array, row_max, col_max, curr, finish, count, visited):
    i, j = curr
    visited[i][j] = True
    if i == finish[0] and j == finish[1]:
        return count
    cnt = row_max * col_max + 1
    if i - 1 >= 0 and array[i - 1][j] == 1 and not visited[i - 1][j]:  # up
        cnt = min(move(array, row_max, col_max, (i - 1, j), finish, count + 1, visited), cnt)
    if i + 1 < row_max and array[i + 1][j] == 1 and not visited[i + 1][j]:  # down
        cnt = min(move(array, row_max, col_max, (i + 1, j), finish, count + 1, visited), cnt)
    if j - 1 >= 0 and array[i][j - 1] == 1 and not visited[i][j - 1]:  # left
        cnt = min(move(array, row_max, col_max, (i, j - 1), finish, count + 1, visited), cnt)
    if j + 1 < col_max and array[i][j + 1] == 1 and not visited[i][j + 1]:  # right
        cnt = min(move(array, row_max, col_max, (i, j + 1), finish, count + 1, visited), cnt)
    return cnt


arr = [[1, 0, 0, 1, 1, 0],
       [1, 0, 0, 1, 0, 0],
       [1, 1, 1, 1, 0, 0],
       [1, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1]]
print(solution(arr, (0, 0), (0, 4)))
