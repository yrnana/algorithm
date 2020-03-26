def leftsmaller(arr, smaller):
    stack = []
    for i in range(len(arr)):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        smaller[i] = stack[-1] if stack else 0
        stack.append(arr[i])


def find_max_diff(arr):
    n = len(arr)
    ls = [0] * n  # 왼쪽에서 자신보다 작은 수 중 가장 가까운 수
    rs = [0] * n  # 오른쪽에서 자신보다 작은 수 중 가장 가까운 수

    leftsmaller(arr, ls)
    leftsmaller(arr[::-1], rs)

    res = -1
    for i in range(n):
        res = max(res, abs(ls[i] - rs[n - 1 - i]))
    return res


print(find_max_diff([2, 4, 8, 7, 7, 9, 3]))
