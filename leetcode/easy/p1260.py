from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        w, h = len(grid[0]), len(grid)
        k %= (w * h)
        if k == 0:
            return grid
        for i in range(h):
            for j in range(w):
                arr.append(grid[i][j])
        arr = arr[-k:] + arr[:-k]
        for i in range(h):
            for j in range(w):
                grid[i][j] = arr[i * w + j]
        return grid
