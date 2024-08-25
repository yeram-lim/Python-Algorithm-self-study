def solution(triangle):
    dp = []
    x, y = 0, 0
    for x in range(len(triangle)):
      row = triangle[x]
      row_nums_count = len(row)
      dp.append([0] * row_nums_count)
      for y in range(0, row_nums_count):
        num = triangle[x][y]
        if x == 0:
          dp[x][y] = num
        elif y == 0:
          dp[x][y] = num + dp[x - 1][y]
        elif y == row_nums_count - 1:
          dp[x][y] = num + dp[x - 1][y - 1]
        elif x > 0 and y > 0:
          dp[x][y] = max(num + dp[x - 1][y - 1], num + dp[x - 1][y])
    
    return max(dp[len(dp) - 1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
  
# 0,0 -> 더할 거 x
# 1,0 -> 7(0,0)
# 1,1 -> 7(0,0)
# 2,0 -> 3(1,0)
# 2,1 -> 3(1,0)+8(1,1)
# 2,2 -> 8(1,1)


# 현재 x,y -> (x,y) + (x-1,y-1) + (x-1,y)

# [[7], 
#  [3, 8], 
#  [8, 1, 0], 
#  [2, 7, 4, 4], 
#  [4, 5, 2, 6, 5]]