def solution(heights):
	heights = [(i + 1, v) for i, v in enumerate(heights)]
	answer = [0]
	stack = [heights[0]]
	for h in heights[1:]:
		while stack and stack[-1][1] <= h[1]:
			stack.pop()
		if not stack:
			answer.append(0)
		else:
			answer.append(stack[-1][0])
		stack.append(h)
	return answer


# answer       stack   h
# [0]          [6]     9
# [0, 0]       [9]     5
# [0, 0, 2]    [9, 5]  7
# [0, 0, 2, 2] [9, 7]  4

print(solution([6, 9, 5, 7, 4]))  # [0,0,2,2,4]
print(solution([3, 9, 9, 3, 5, 7, 2]))  # [0,0,0,3,3,3,6]
print(solution([1, 5, 3, 6, 7, 6, 5]))  # [0,0,2,0,0,5,6]
