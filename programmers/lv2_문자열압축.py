from math import floor


def solution(s):
    if len(s) == 1:
        return 1
    answer = float('inf')
    for d in range(floor(len(s) // 2), 0, -1):  # d : 나누는 수
        tmp = []
        i = 0
        while i < len(s):
            tmp.append(s[i:i + d])
            i += d
        cnt, curr_cnt, prev = 0, 1, tmp[0]
        for j in range(1, len(tmp)):
            if prev == tmp[j]:
                curr_cnt += 1
            else:
                cnt += d
                if curr_cnt != 1:
                    cnt += len(str(curr_cnt))
                prev = tmp[j]
                curr_cnt = 1
            if j == len(tmp) - 1:
                if curr_cnt == 1:
                    cnt += len(tmp[-1])
                else:
                    cnt += d + len(str(curr_cnt))
            if cnt > answer:
                break
        answer = min(answer, cnt)
    return answer


# print(solution('aabbaccc'))  # 7 : 2a2b3c, 1
# print(solution('ababcdcdababcdcd'))  # 9 : 2ababcdcd, 8
# print(solution('abcabcdede'))  # 8 : 2abcdede, 3
# print(solution('abcabcabcabcdededededede'))  # 14 : 2abcabc2dedede, 6
# print(solution('xababcdcdababcdcd'))  # 17 : x
print(solution('a'))
