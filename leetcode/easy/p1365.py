from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indices = {}
        for idx, num in enumerate(sorted(nums)):
            indices.setdefault(num, idx)
        return [indices[num] for num in nums]
        # answer = [0] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] > nums[j]:
        #             answer[i] += 1
        # return answer


solution = Solution()
print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
print(solution.smallerNumbersThanCurrent([6, 5, 4, 8]))
print(solution.smallerNumbersThanCurrent([7, 7, 7, 7]))
