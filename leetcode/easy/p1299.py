from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = []
        i, l = 0, len(arr)
        while i < l - 1:
            max_val, max_idx = 0, 0
            for j, x in enumerate(arr[i + 1:l]):
                if x >= max_val:
                    max_idx = j
                    max_val = x
            max_idx += i + 1
            for x in range(max_idx - i):
                answer.append(max_val)
            i = max_idx
        answer.append(-1)
        return answer
