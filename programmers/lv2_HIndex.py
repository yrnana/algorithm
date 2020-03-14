def solution(citations):
	max_val = max(citations)
	for h in range(max_val, 1, -1):
		cnt = 0
		for x in citations:
			if x >= h:
				cnt += 1
		if cnt >= h:
			return h
	return 0


print(solution([22, 42]))  # 2
print(solution([20, 19, 18, 1]))  # 3
print(solution([3, 0, 6, 1, 5]))
print(solution([2, 0, 6, 1, 5, 7]))
print(solution([2, 0, 6, 1, 5, 7, 9]))
