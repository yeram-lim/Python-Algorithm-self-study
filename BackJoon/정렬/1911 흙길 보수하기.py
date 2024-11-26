import heapq
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
puddles = []
for i in range(N):
  start, end = map(int, input().split())
  heapq.heappush(puddles, (start, end))

start, end = heapq.heappop(puddles)
last_covered_position = start - 1
board_count = 0
while True:
  covered_position = last_covered_position + L
  last_covered_position = covered_position
  board_count += 1
  
  if covered_position >= end - 1:
    if len(puddles) > 0:
      start, end = heapq.heappop(puddles)
      if last_covered_position < start:
        last_covered_position = start - 1
    else:
      break
    
print(board_count)