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
#     answer = 0
#     tmp = string[0]
#     for x in string[1:]:
#         if x in tmp:
#             answer = max(answer, len(tmp))
#             tmp = x
#         else:
#             tmp += x
#     return answer


print(solution('aabcbcbc'))
print(solution('aaaaaaaa'))
print(solution('abbbcedd'))
