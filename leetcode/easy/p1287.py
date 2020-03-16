from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        import bisect
        n = len(arr) // 4
        for i in range(0, len(arr), n + 1):
            # print(n, i, arr[i], bisect.bisect(arr, arr[i]), bisect.bisect_left(arr, arr[i]))
            if bisect.bisect(arr, arr[i]) - bisect.bisect_left(arr, arr[i]) > n:
                return arr[i]


s = Solution()
# print(s.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(s.findSpecialInteger([1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 7, 9, 10]))
