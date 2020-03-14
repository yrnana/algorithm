from collections import Counter


def solution(nums):
	c = Counter(nums)
	length = len(nums) // 2
	key_len = len(c.keys())
	return length if key_len >= length else key_len


print(solution([3, 1, 2, 3]))  # 2
print(solution([3, 3, 3, 2, 2, 4]))  # 3
print(solution([3, 3, 3, 2, 2, 2]))  # 2
