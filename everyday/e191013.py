def solution(arr):
	if len(arr) < 2:
		return float('-inf')
	max1 = max(arr[0], arr[1])
	max2 = float('-inf')
	for x in arr[1:]:
		if x > max1:
			max2 = max1
			max1 = x
		elif x > max2 and x != max1:
			max2 = x
	return max2


print(solution([10, 5, 4, 3, -1]))
print(solution([3, 3, 3]))
