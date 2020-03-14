def solution(arr):
	l = len(arr)
	answer, arr1, arr2 = [0] * l, [1] * l, [1] * l

	for i in range(l - 1):
		arr1[i + 1] = arr1[i] * arr[i]

	for i in range(l - 1, 0, -1):
		arr2[i - 1] = arr2[i] * arr[i]

	for i in range(l):
		answer[i] = arr1[i] * arr2[i]

	return answer


print(solution([1, 2, 3, 4, 5]))
