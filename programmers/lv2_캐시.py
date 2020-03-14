from collections import deque


def solution(cacheSize, cities):
	answer = 0
	if cacheSize == 0:
		return len(cities) * 5
	deq = deque(maxlen=cacheSize)
	for city in cities:
		low_city = city.lower()
		if low_city in deq:  # hit
			answer += 1
			i = deq.index(low_city)
			el = deq[i]
			del deq[i]
			deq.appendleft(el)
		else:
			answer += 5
			if len(deq) == cacheSize:
				deq.pop()
			deq.appendleft(low_city)

	return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 25
