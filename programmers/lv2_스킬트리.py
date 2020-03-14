def solution(skill, skill_trees):
    answer = 0
    d = dict()
    for i in range(len(skill)):
        d[skill[i]] = str(i)
    for tree in skill_trees:
        s = ''
        for x in tree:
            if x in skill:
                s += d[x]
        if s == '':
            answer += 1
        else:
            l = len(s)
            tmp = ''
            for i in range(l):
                tmp += str(i)
            if tmp == s:
                answer += 1
    return answer


print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))
