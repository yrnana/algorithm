import heapq


def solution(scoville, K):
	answer = 0
	heap = scoville
	heapq.heapify(heap)
	while len(heap) >= 2:
		a = heapq.heappop(heap)
		if a >= K:
			break
		b = heapq.heappop(heap)
		new = a + b * 2
		heapq.heappush(heap, new)
		answer += 1
	return -1 if heap[0] < K else answer
