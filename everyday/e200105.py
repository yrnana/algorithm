def solution(arr):
    c = 0
    l = len(arr)
    i = 0
    while True:
        c += 1
        k = arr[i]
        if k == 0 or i == k:
            break
        i = k
    return c == l


print(solution([1, 2, 4, 0, 3]))
print(solution([1, 4, 5, 0, 3, 2]))
print(solution([1, 2, 2, 0]))
print(solution([1, 2, 2]))
