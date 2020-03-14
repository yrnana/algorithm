arr = [2, 5, 6, 1, 10]
target = 8
memo = dict()

for i, x in enumerate(arr):
    if target - x in memo:
        print([memo.get(target - x), i])
        break
    memo[x] = i
