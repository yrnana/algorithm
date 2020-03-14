def solution(n, words):
	prev = []
	pn = 0  # person_number

	for i in range(len(words)):
		w = words[i]
		if prev and prev[-1][-1] != w[0] or w in prev:
			return [pn + 1, i // n + 1]
		pn = (pn + 1) % n
		prev.append(w)

	return [0, 0]


print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))  # [3,3]
print(solution(5,
               ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang',
                'gather', 'refer', 'reference', 'estimate', 'executive']))  # [0,0]
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))  # [1,3]
