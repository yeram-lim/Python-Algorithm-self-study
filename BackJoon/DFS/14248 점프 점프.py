import sys
input = sys.stdin.readline # input함수 빠르게

N = int(input())
stone_list = list(map(int, input().split()))
position = int(input()) - 1

visited = []

def bfs(position):
  if position not in visited:
    step = stone_list[position]
    visited.append(position)
    next_1 = position + step
    next_2 = position - step
    if not (next_1 < 0 or next_1 >= N):
      bfs(next_1)
    if not (next_2 < 0 or next_2 >= N):
      bfs(next_2)
    
bfs(position)
print(len(visited))

# print(visited)

# 5
# 1 4 2 2 1
# 3