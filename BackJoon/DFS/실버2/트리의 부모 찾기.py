import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
graph = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

for i in range(N - 1):
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

def dfs(parent):
  children_nodes = graph[parent] #[6, 4]
  for child in children_nodes:
    if parents[child] == 0:
      parents[child] = parent
      dfs(child)
dfs(1)

for j in range(2, len(parents)):
    print(parents[j])

# print(graph,parents)

