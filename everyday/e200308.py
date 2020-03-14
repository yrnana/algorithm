# https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/


import heapq
from collections import Counter


def solution(string):
	ans = ''

	c = Counter(string)
	pq = [(-v, k) for k, v in c.items()]  # highest frequency char to first
	heapq.heapify(pq)  # maxheap

	prev = (1, '#')  # create temp key that will be used as the prev visited element
	while any(pq):
		# pop top element from maxheap and add it to string
		f, e = heapq.heappop(pq)
		ans += e
		# if freq > 0, push back
		if prev[0] < 0:
			heapq.heappush(pq, prev)
		#  make current character as the prev
		f += 1
		prev = (f, e)

	if len(string) != len(ans):
		return ''
	else:
		return ans


# Priority Queue
print(solution('aaabbc'))  # ababac
print(solution('aaac'))  # ''
print(solution('aaabc'))  # abaca
print(solution('aaabb'))  # ababa
print(solution('aaaabc'))  # ''
