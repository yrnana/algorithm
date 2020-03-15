class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        tmp = [[False] * m for x in range(n)]
        for [x, y] in indices:
            for i in range(m):
                tmp[x][i] = not tmp[x][i]
            for i in range(n):
                tmp[i][y] = not tmp[i][y]
        answer = 0
        for i in range(n):
            for j in range(m):
                if tmp[i][j]:
                    answer += 1
        return answer
