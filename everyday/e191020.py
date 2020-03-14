def solution(arr):
	l = len(arr)
	n = 0
	for i in range(l):
		if arr[i] != 0:
			swap(arr, i, n)
			n += 1
	return arr


def swap(arr, i, j):
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp


print(solution([0, 5, 0, 3, -1]))
print(solution([3, 0, 3]))
