def dfs(answer, adj, src, cnt):
    answer.append(src)
    if cnt == 0:  # 티켓을 다 썼다면
        return True
    for i in range(len(adj[src])):
        dist = adj[src].popleft()
        if dfs(answer, adj, dist, cnt - 1):
            return True
        adj[src].append(dist)
    answer.pop()
    return False


def solution(tickets):
    from collections import defaultdict, deque
    answer = []
    adj = defaultdict(deque)
    for src, dist in tickets:
        adj[src].append(dist)
    for k, v in adj.items():
        adj[k] = deque(sorted(v))
    dfs(answer, adj, 'ICN', len(tickets))
    return answer


# def dfs(answer, src, tickets):
#     answer.append(src)
#     if not tickets:
#         return True
#     i = 0
#     while tickets and i < len(tickets):
#         if tickets[i][0] == src:
#             x = tickets.pop(i)
#             if dfs(answer, x[1], tickets):
#                 return True
#             tickets.insert(i, x)  # 티켓사용실패시 원복
#         i += 1
#     answer.pop()
#     return False
#
#
# def solution(tickets):
#     answer = []
#     tickets.sort(key=lambda x: (x[0], x[1]))
#     dfs(answer, 'ICN', tickets)
#     return answer


# print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]))
# print(solution([['ICN', 'SFO'], ['SFO', 'ICN'], ['ICN', 'SFO'], ['SFO', 'QRE']]))
# print(solution([['ICN', 'COO'], ['ICN', 'BOO'], ['COO', 'ICN'], ['BOO', 'DOO']]))
