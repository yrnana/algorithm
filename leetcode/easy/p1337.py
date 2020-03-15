from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        w, h = len(mat[0]), len(mat)
        tmp = []
        for i in range(h):
            cnt = 0
            for j in range(w):
                if mat[i][j] == 1:
                    cnt += 1
            tmp.append((i, cnt))
        tmp.sort(key=lambda x: x[1])
        return list(map(lambda x: x[0], tmp[:k]))
