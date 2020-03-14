def solution(s):
	stack = [s[0]]
	for i in range(1, len(s)):
		if s[i] == '(':
			stack.append('(')
		else:
			if stack and stack[-1] == '(':
				stack.pop()
			else:
				return False
	return False if stack else True


print(solution('('))
print(solution('()()'))  # true
print(solution('(())()'))  # true
print(solution(')()('))  # false
print(solution('(()('))  # false
