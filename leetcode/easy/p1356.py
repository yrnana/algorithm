from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        tmp = []
        for x in arr:
            cnt = 0
            n = x
            while n > 0:
                if n % 2 == 1:
                    cnt += 1
                n //= 2
            tmp.append((cnt, x))
        tmp.sort(key=lambda x: (x[0], x[1]))
        return list(map(lambda x: x[1], tmp))
