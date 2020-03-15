from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        for i in range(len(points) - 1):
            s, e = points[i], points[i + 1]
            dx, dy = abs(s[0] - e[0]), abs(s[1] - e[1])
            answer += max(dx, dy)
        return answer
