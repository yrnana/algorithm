from functools import cmp_to_key


def sort_func(a, b):
	if a == b:
		return 0
	x, y = a + b, b + a
	if x == y:
		return 1
	elif x > y:
		return -1
	else:
		return 1


def solution(numbers):
	numbers = list(map(str, numbers))
	numbers.sort(key=cmp_to_key(sort_func))
	answer = ''.join(numbers)
	for x in answer:
		if x != '0':
			return answer
	return '0'


# print('30' > '3') # True
# print('30' < '4') # True
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0, 0]))
print(solution([12, 121]))  # 12121
print(solution([21, 212]))  # 21221
