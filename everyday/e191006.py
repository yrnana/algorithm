def sol(string):
	answer = ''
	tmp = ''
	for s in string:
		if s == ' ':
			answer += tmp + ' '
			tmp = ''
		else:
			tmp = s + tmp
	return answer + tmp


print(sol('abc 123 apple'))
