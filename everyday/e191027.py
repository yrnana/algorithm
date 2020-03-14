def solution(string):
	answer = 0
	start = 0
	d = dict()
	for i in range(len(string)):
		c = string[i]
		if c in d:
			start = max(start, d[c])
		answer = max(answer, i - start + 1)
		d[c] = i + 1
	return answer


# def solution(string):
# 	d = dict()  # char: int
# 	s, e = 0, 0
# 	for i in range(len(string)):
# 		c = string[i]
# 		# print(d, s, e, i, c)
# 		if c in d:
# 			s = max(d[c], s)
# 		e = max(e, i - s + 1)
# 		d[c] = i + 1
# 	return e


print(solution('aabcbcbc'))
print(solution('aaaaaaaa'))
print(solution('abbbcedd'))
