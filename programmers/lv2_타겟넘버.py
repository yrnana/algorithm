def preorder(arr, prev, i, sign, target, answer):
    if i < len(arr):
        while len(prev) > i:
            prev.pop()
        prev.append(arr[i] * sign)
        if len(prev) == len(arr) and sum(prev) == target:
            answer[0] += 1
        preorder(arr, prev, i + 1, -1, target, answer)
        preorder(arr, prev, i + 1, 1, target, answer)


def solution(numbers, target):
    answer = [0]
    preorder(numbers, [], 0, 1, target, answer)
    preorder(numbers, [], 0, -1, target, answer)
    return answer[0]


print(solution([1, 1, 1, 1, 1], 3))
