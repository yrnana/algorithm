def solution(arr, N):
    return quickselect(arr, 0, len(arr) - 1, N - 1)


def quickselect(arr, l, r, k):
    if l <= r:
        pivot = partition(arr, l, r)
        if pivot == k:
            return arr[k]
        if pivot > k:
            return quickselect(arr, l, pivot - 1, k)
        return quickselect(arr, pivot + 1, r, k)
    return float('-inf')


def partition(arr, l, r):
    p = l
    for j in range(l, r):
        if arr[j] > arr[r]:
            arr[p], arr[j] = arr[j], arr[p]
            p += 1
    arr[p], arr[r] = arr[r], arr[p]
    return p


print(solution([-1, 3, -1, 5, 4], 2))
print(solution([2, 4, -2, -3, 8], 1))
print(solution([-5, -3, 1], 3))
