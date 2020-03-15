from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums) - 1, 2):
            answer += [nums[i + 1]] * nums[i]
        return answer


solution = Solution()
print(solution.decompressRLElist([1, 2, 3, 4]))  # [2,4,4,4]
print(solution.decompressRLElist([1, 1, 2, 3]))  # [1,3,3]
