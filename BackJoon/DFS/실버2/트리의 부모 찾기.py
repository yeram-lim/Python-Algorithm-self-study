from collections import deque


N = int(input())
graph = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

for i in range(N - 2):
  node1, node2 = list(map(int, input().split()))
  graph[node1].append(node2)
  graph[node2].append(node1)

q = deque()
for i in range(1, N + 1):
  children_nodes = graph[i]
  for child in children_nodes:
    graph[child] = i
    

print(graph)
# [[], [6, 4], [4], [6, 5], [1, 2], [3], [1, 3], []]

