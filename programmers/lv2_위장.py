def solution(clothes):
    answer = 1
    d = dict()
    for x in clothes:
        if x[1] in d:
            d[x[1]] += 1
        else:
            d[x[1]] = 1
    for x in d.values():
        answer *= x + 1
    return answer - 1


print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))
