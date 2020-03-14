def solution(s):
	stack = []
	for c in s:
		if stack and stack[-1] == c:
			stack.pop()
		else:
			stack.append(c)
	return 0 if len(stack) > 0 else 1


print(solution('baabaa'))
print(solution('cdcd'))
