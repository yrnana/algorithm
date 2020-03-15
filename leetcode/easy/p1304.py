from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        k = n // 2
        if n % 2 == 0:
            return [i for i in range(-k, 0)] + [i for i in range(1, k + 1)]
        else:
            return [i for i in range(-k, k + 1)]
