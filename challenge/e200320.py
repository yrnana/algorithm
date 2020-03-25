def solution(numbers, target):
    def recur(nums, t, prev, i):
        if i == len(nums):
            return 1 if prev == t else 0
        return recur(nums, t, prev + nums[i], i + 1) + recur(nums, t, prev - nums[i], i + 1)

    return recur(numbers, target, 0, 0)


print(solution([1, 1, 1, 1, 1], 3))  # 5
# print(solution([1, 1, 1], 3))  # 5
