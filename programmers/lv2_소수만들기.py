from itertools import combinations


def is_prime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i ** 2 <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True


def solution(nums):
	answer = 0
	c = combinations(nums, 3)
	c = list(map(sum, c))
	for x in c:
		if is_prime(x):
			answer += 1
	return answer


print(solution([1, 2, 3, 4]))  # 1
print(solution([1, 2, 7, 6, 4]))  # 4
