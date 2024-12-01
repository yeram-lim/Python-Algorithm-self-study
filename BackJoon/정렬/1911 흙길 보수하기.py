import heapq
import math
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
puddles = []
for i in range(N):
  start, end = map(int, input().split())
  heapq.heappush(puddles, (start, end))
last_covered_boundary = puddles[0][0]
total_board_count = 0
while len(puddles) > 0:
  puddle = heapq.heappop(puddles)
  start, end = puddle
  
  if last_covered_boundary > end:
    continue
  
  if last_covered_boundary < start:
    last_covered_boundary = start
  
  needed_cover_size = end - last_covered_boundary
  board_count = math.ceil(needed_cover_size / L)
  total_board_count += board_count
  last_covered_boundary += board_count * L
print(total_board_count)
# start, end = heapq.heappop(puddles)
# last_covered_boundary = start - 1
# board_count = 0
# while True:
#   # print('🍎last_covered_boundary:',last_covered_boundary,'board_count:',board_count)
#   if last_covered_boundary < start - 1 and last_covered_boundary < end - 1:
#     last_covered_boundary = start - 1

#   covered_boundary = last_covered_boundary + L
#   last_covered_boundary = covered_boundary
#   board_count += 1
  
#   if covered_boundary >= end - 1:
#     if len(puddles) > 0:
#       start, end = heapq.heappop(puddles)
#     else:
#       break
    
# print(board_count)

# # 3 3
# # 1 6
# # 13 17
# # 8 12