from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        from collections import Counter
        c = Counter(chips)
        odd, even = 0, 0
        for k, v in c.items():
            if k % 2 == 0:
                odd += v
            else:
                even += v
        return min(odd, even)
