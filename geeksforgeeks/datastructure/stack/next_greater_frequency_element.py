from collections import Counter


def solution(arr):
    freq = Counter(arr)
    print(freq)

    n = len(arr)
    result = [0] * n

    stack = [0]
    for i in range(1, n):
        while stack and freq[arr[stack[-1]]] < freq[arr[i]]:  # stack의 freq가 더 작다면
            result[stack.pop()] = arr[i]
        stack.append(i)

    while stack:
        result[stack.pop()] = -1

    return result


print(solution([1, 1, 2, 3, 4, 2, 1]))  # [-1, -1, 1, 2, 2, 1, -1]
