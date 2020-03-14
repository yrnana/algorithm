def solution(number, k):
	answer = ''
	l = len(number)
	n = l - k  # 반환해야 할 문자열의 길이
	a, b = -1, '-1'
	for i in range(n):
		for j in range(a + 1, l - (n - i) + 1):  # 큰 수를 찾은 자리 이후부터 맨 뒤의 n - i - 1 자리를 제외하고
			if b < number[j]:  # 제일 큰 수를 찾는다
				b = number[j]
				a = j
				if b == '9':  # 최대값 9를 찾으면 루프 종료
					break
		answer += b
		b = '-1'  # 최대값 초기화
	return answer


print(solution('19245', 2))  # 945
print(solution('1924', 2))  # 94
print(solution('1231234', 3))  # 3234
print(solution('3112534', 3))  # 3534
print(solution('4177252841', 4))  # 775841
