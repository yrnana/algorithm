from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] < 0:
                answer += (m - i) * n
                break
            for j in range(n):
                if grid[i][j] < 0:
                    answer += n - j
                    break
        return answer
