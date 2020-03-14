# LZW 압축은 다음 과정을 거친다.
# 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# 3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 5. 단계 2로 돌아간다.


def solution(msg):
	answer = []
	max_idx = 26
	d = dict()
	for i in range(1, max_idx + 1):
		d[chr(i + 64)] = i
	l = len(msg)
	i = 0
	while i < l:
		j = i + 2
		while j <= l and msg[i:j] in d:  # msg[i:j] : 사전에 없는 수
			j += 1
		answer.append(d[msg[i:j - 1]])  # 출력
		max_idx += 1  # 최대 색인값 증가
		d[msg[i:j]] = max_idx
		i = j - 1
	return answer


print(solution('KAKAO'))  # [11, 1, 27, 15]
print(solution('TOBEORNOTTOBEORTOBEORNOT'))  # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution('ABABABABABABABAB'))  # [1, 2, 27, 29, 28, 31, 30]
