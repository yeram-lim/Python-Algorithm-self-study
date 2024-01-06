# 2차 시도
def solution(maps):
    answer = -1
    n = len(maps[0]) - 1
    m = len(maps) - 1
    
    visited = [[-1 for j in range(n + 1)] for i in range(m + 1)]
    
    def bfs(x, y, count):
        nonlocal answer
        nonlocal visited
        
        if x == n and y == m:
            if answer == -1 or answer > count:
                answer = count
            return
        if count != -1 and answer == (n + m + 1):
            return
        if maps[y][x] == 0 or (visited[y][x] != -1 and count > visited[y][x]):
            return
        
        if visited[y][x] == -1 or visited[y][x] > count:
            visited[y][x] = count
        count += 1
        if x < n:
            bfs(x + 1, y, count)
        if x > 0:
            bfs(x - 1, y, count)
        if y < m:
            bfs(x, y + 1, count)
        if y > 0:
            bfs(x, y - 1, count)
    
    bfs(0, 0, 1)
    
    return answer

# print(solution([[1, 1, 0], [1, 0, 0], [1, 1, 1]]))
print(solution([
                [1,1,1,1,1],
                [1,0,1,1,1],
                [1,0,1,0,1],
                [1,1,1,1,1],
                [0,0,0,0,1]
                ]))


# 1차 시도
# def solution(maps):
#     answer = -1

#     def visit(x, y, count):
#         # print('🍎',x,y,count)
#         if maps[x][y] == 1:
#             count += 1
#             maps[x][y] = -1 
#             if x == len(maps) - 1 and y == len(maps) - 1:
#                 if answer > 0 and count < answer:
#                     return count
#                 else:
#                     return -1
#             if x + 1 < len(maps):
#                 visit(x + 1, y, count)
#             if x - 1 >= 0:
#                 visit(x - 1, y, count)
#             if y + 1 < len(maps):
#                 visit(x, y + 1, count)
#             if y - 1 >= 0:
#                 visit(x, y - 1, count)
            
#     answer = visit(0, 0, 0)
#     print(answer)
        
#     return answer if answer else -1
  
# solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])