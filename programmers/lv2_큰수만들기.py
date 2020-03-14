def solution(number, k):
	temp = list()
	for num in number:
		while k > 0 and temp and temp[-1] < num:
			temp.pop()
			k -= 1
		temp.append(num)
	while k > 0:
		temp.pop()
		k -= 1
	return ''.join(temp)


# print(solution('1924', 2))
# print(solution('1231234', 3))
print(solution('4177252841', 4))
