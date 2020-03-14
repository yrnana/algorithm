def solution(array):
    ans = []
    row, col = len(array), len(array[0])
    x, y = 0, 0
    a, b, c, d = col, row - 1, col - 1, row - 2
    l = row * col
    while l >= len(ans):
        for i in range(a):
            ans.append(array[y][x])
            if l <= len(ans):
                return ans
            x += 1
        x -= 1
        y += 1
        for i in range(b):
            ans.append(array[y][x])
            if l <= len(ans):
                return ans
            y += 1
        y -= 1
        x -= 1
        for i in range(c):
            ans.append(array[y][x])
            if l <= len(ans):
                return ans
            x -= 1
        x += 1
        y -= 1
        for i in range(d):
            ans.append(array[y][x])
            if l <= len(ans):
                return ans
            y -= 1
        y += 1
        x += 1
        a -= 2
        b -= 2
        c -= 2
        d -= 2
    return ans


arr = [[1, 2, 3],
       [8, 9, 4],
       [7, 6, 5]]
# 5 3 4 2 / 3 1 2
arr = [[1, 2, 3, 4, 5],
       [14, 15, 16, 17, 6],
       [13, 20, 19, 18, 7],
       [12, 11, 10, 9, 8]]
print(solution(arr))
