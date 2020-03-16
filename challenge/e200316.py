def recur(arr, curr, i, max_val):
    if i == 3:
        arr.append(curr)
        return
    for j in range(1, max_val[i] + 1):
        recur(arr, curr + j, i + 1, max_val)


def solution(monster, S1, S2, S3):
    from math import floor
    monster = list(map(lambda x: x - 1, monster))
    res = []
    recur(res, 0, 0, [S1, S2, S3])
    cnt = 0
    for n in res:
        if n in monster:
            cnt += 1
    return floor(((len(res) - cnt) / len(res)) * 1000)


# 1~2 1~3 1~4 = 24
# 1~2 1~3 1~3 = 18
print(solution([4, 9, 5, 8], 2, 3, 4))  # 500 1/2
print(solution([4, 9, 5, 8], 2, 3, 3))  # 555 5/9
