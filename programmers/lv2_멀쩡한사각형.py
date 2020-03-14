from math import gcd


def solution(w, h):
	g = gcd(w, h)
	print(w, h, g)
	return w * h - (w + h - g)


print(solution(8, 12))  # 80 = 8 * 12 - 4 * 4(gcd)
print(solution(4, 4))  # 12 = 4 * 4 - 1 * 4(gcd)
print(solution(3, 4))  # 6 = 3 * 4 - 6 * 1
print(solution(3, 5))  # 8 = 3 * 5 - 7 * 1
