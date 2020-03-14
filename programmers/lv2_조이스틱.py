def solution(name):
	answer = 0
	n = len(name)
	turn = n - 1  # 최대이동횟수
	for i in range(n):
		if name[i] != 'A':
			move = ord(name[i]) - ord('A')
			if move > 13:
				move = 25 - move + 1
			answer += move
		next = i + 1  # 다음 문자 idx
		while next < n and name[next] == 'A':
			next += 1  # A인 경우 계속 오른쪽으로 이동
		turn = min(turn, i + n - next + min(i, n - next))
	return answer + turn


print(solution('BBAAAAABB'))  # 3
# print(solution('B'))  # 1
# print(solution('BA'))  # 1
# print(solution('AAZ'))  # 2
# print(solution('AAA'))  # 0
# print(solution('ABAAA'))  # 2
# print(solution('AAAAAZ'))  # 2
# print(solution('JAZ'))  # 11
# print(solution('JAAZ'))  # 11
# print(solution('JEROEN'))  # 56
# print(solution('JAN'))  # 23
# print(solution('XXAAAAAAAAAAAXX'))
# print(solution('XXXAAAAXX'))
