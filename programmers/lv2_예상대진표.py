from math import ceil


def solution(n, a, b):
	answer = 1
	i, j = a, b  # 현재참가자번호
	while n >= 2:
		if i > j:  # x > y
			x, y = i, j
		else:
			x, y = j, i
		if x - y == 1 and x % 2 == 0:
			break
		i = ceil(i / 2)
		j = ceil(j / 2)
		answer += 1
		n //= 2

	return answer


print(solution(8, 4, 7))
