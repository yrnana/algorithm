def solution(path):
    path_list = path.split('/')
    ans = []
    for x in path_list[1:-1]:
        if x == '.':
            pass
        elif x == '..':
            ans.pop()
        else:
            ans.append(x)
    return '/' + '/'.join(ans) + '/'


print(solution('/usr/bin/../'))
print(solution('/usr/./bin/./test/../'))
