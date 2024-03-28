import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
graph = [[] for _ in range(N + 1)] #[[], [(3, 2)], [(3, 1), (2, 3), (4, 4)], [(2, 2)], [(4, 2)]]
distances = [0 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for i in range(N - 1):
    start, end, distance = map(int, input().split())
    graph[start].append((distance, end))
    graph[end].append((distance, start))
# print(graph)

def dfs(current, distance, visited): 
    # print('visited : ',visited)
    # new_visited = visited.append(current)
    visited[current] = 1
    next_nodes = graph[current] # 1: [(3, 2)] / 2: [(3, 1), (2, 3), (4, 4)]
    for next in next_nodes:
        next_distance, next_node = next
        # print('🍎next : ',next_distance, next_node,visited, visited[next_node])
        if not visited[next_node]:
            total_distance = distance + next_distance #1: 3 / 2: x, 5, 7
            dfs(next_node, total_distance, visited) # 1: (2,3,[1]) 2: (3,5,[1,2]),(4,7,[1,2])
    if distances[current] < distance:
        distances[current] = distance
    # print('🍊 distances :', distances)

dfs(1, 0, visited)
print(max(distances))


# 4
# 1 2 3
# 2 3 2
# 2 4 4