from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        c = Counter(arr)
        key = []
        for x in c.values():
            if x in key:
                return False
            key.append(x)
        return True
