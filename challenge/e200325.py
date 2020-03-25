# i가 속한 집합의 head 반환
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


# x와 y가 속한 집합을 하나로 합친다 (깊이가 적은 트리를 깊은 트리의 루트 아래 추가)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def solution(n, costs):
    # 크루스칼 알고리즘 (minimum spanning tree)
    answer = 0
    parent, rank = [], []
    costs.sort(key=lambda a: a[2])

    for node in range(n):
        parent.append(node)  # [0, 1, 2, 3]
        rank.append(0)  # [0, 0, 0, 0]

    i, j = 0, 0
    while i < len(costs) and j < n - 1:
        src, dist, cost = costs[i]
        i += 1
        x, y = find(parent, src), find(parent, dist)
        if x != y:
            j += 1
            answer += cost
            union(parent, rank, x, y)
    return answer


# print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))  # 4
print(solution(9, [[7, 6, 1], [8, 2, 2], [6, 5, 2], [0, 1, 4], [2, 5, 4], [8, 6, 6], [2, 3, 7], [7, 8, 7], [0, 7, 8],
                   [1, 2, 8], [3, 4, 9], [5, 4, 10], [1, 7, 11], [3, 5, 14]]))
