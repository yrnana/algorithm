import heapq


# 기간내에 여러개의 날에서 공급을 받을 수 있다면 가장 많은 양을 받아온다
def solution(stock, dates, supplies, k):
	answer = 0
	d = 0
	heap = []
	while stock < k:
		for j in range(d, len(dates)):
			if dates[j] <= stock:
				heapq.heappush(heap, -supplies[j])
				d = j + 1
			else:
				break
		stock -= heapq.heappop(heap)
		answer += 1
	return answer


print(solution(4, [4, 10, 15], [20, 5, 10], 30))  # 2
