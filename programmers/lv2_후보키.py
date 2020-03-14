# 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
# 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.


from itertools import combinations


def is_cand_key(relation, key_arr):
	tmp_arr = []
	for row in relation:
		tmp = []
		for k in key_arr:
			tmp.append(row[k])
		tmp = '+'.join(tmp)
		if tmp in tmp_arr:
			return False
		tmp_arr.append(tmp)
	return True


def key_is_subset(key, keys):
	for k in keys:
		if k.issubset(key):
			return False
	return True


def solution(relation):
	w = len(relation[0])  # 키의 경우의 수 2^4-1=15
	column = [x for x in range(w)]
	keys = []
	for n in range(1, w + 1):
		c = [set(x) for x in combinations(column, n)]
		tmp_key = []
		for key in c:
			if key_is_subset(key, keys):
				tmp_key.append(key)
		for key in tmp_key:
			if is_cand_key(relation, key):
				keys.append(key)
	return len(keys)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))  # 2
print(solution([['a', 'b', 'c'], ['1', 'b', 'c'], ['a', 'b', '4'], ['a', '5', 'c']]))  # 1
print(solution([['a', '1', '4'], ['2', '1', '5'], ['a', '2', '4']]))  # 2
