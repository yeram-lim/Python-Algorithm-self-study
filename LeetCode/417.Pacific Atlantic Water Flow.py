# 2차 시도
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        answer = []
        direction_x = [-1, 0, 1, 0]
        direction_y = [0, -1, 0, 1]
        x_length = len(heights)
        y_length = len(heights[0])

        p_visited = []
        a_visited = []

        def dfs(x, y, direction, sea):
            if sea == 'p':
                if [x, y] not in p_visited:
                    p_visited.append([x, y])
            else:
                if [x, y] not in a_visited:
                    a_visited.append([x, y])

            next_x = x
            next_y = y
            
            if direction == 'right':
                next_y += 1
            elif direction == 'left':
                next_y -= 1
            elif direction == 'down':
                next_x += 1
            elif direction == 'up':
                next_x -= 1

            if not (next_x < 0 or next_x > x_length - 1 or next_y < 0 or next_y > y_length - 1):
                height = heights[x][y]
                next_height = heights[next_x][next_y]

                if height <= next_height:
                    dfs(next_x, next_y, direction, sea)
            # elif not (x < 0 or x > x_length - 1 or y < 0 or y > y_length - 1):
            #     dfs(next_x, next_y, direction, sea)
                
        # 왼편 Pacific, 오른편 Atlantic에서 출발
        for i in range(x_length):
            dfs(i, 0, 'right', 'p')
            dfs(i, y_length - 1, 'left', 'a')

            # short = p_visited if len(p_visited) < len(a_visited) else a_visited
            # for position in p_visited:
            #     if position in a_visited:
            #         answer.append(position)
        
        # 위편 Pacific, 아래편 Atlantic에서 출발
        for i in range(y_length):
            dfs(0, i, 'down', 'p')
            # print('p 끝나고', p_visited, a_visited)
            dfs(x_length - 1, i, 'up', 'a')
            # print('a 끝나고', p_visited, a_visited)

        for position in p_visited:
            if position in a_visited:
                if position not in answer:
                    answer.append(position)
        

        print(p_visited)
        print( a_visited)
        print(answer)

a = Solution()
b = a.pacificAtlantic([[1,2,2,3,5],
                       [3,2,3,4,4],
                       [2,4,5,3,1],
                       [6,7,1,4,5],
                       [5,1,1,2,4]])
# 답 [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# b = a.pacificAtlantic([[1,2,2],[3,2,3],[2,4,5]])

# 1차 시도
# from typing import List


# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         answer = []
#         direction_x = [-1, 0, 1, 0]
#         direction_y = [0, -1, 0, 1]
#         x_length = len(heights)
#         y_length = len(heights[0])

#         # 0번째에 pacific 갔는지 유무 저장
#         # 1번째에 atlantic 갔는지 유부 저장
#         visited = [[0 for i in range(y_length)] for i in range(x_length)]
#         can_approach_water = [[[0, 0] for i in range(y_length)] for i in range(x_length)]
        
#         # 바다 방향 확인
#         def bfs(x, y, start, start_height):
#             nonlocal can_approach_water
#             nonlocal visited
#             # if x == start[0] and y == start[1]:
#             visited[x][y] = 1

#             for i in range(4):
#                 dx = x + direction_x[i]
#                 dy = y + direction_y[i]

#                 if not (dx < 0 or dx > x_length - 1 or dy < 0 or dy > y_length - 1):
#                     if visited[dx][dy] != 1:
#                         curr_height = start_height
#                         next_height = heights[dx][dy]
#                         if curr_height >= next_height:
#                             # a=''
#                             bfs(dx, dy, start, next_height)
#                         else:
#                             bfs(dx, dy, (dx, dy), next_height)

#                 else:
#                     if dx < 0 or dy < 0:
#                         can_approach_water[start[0]][start[1]][0] = 1
#                     else:
#                         can_approach_water[start[0]][start[1]][1] = 1
#                     if can_approach_water[start[0]][start[1]][0] == 1 and can_approach_water[start[0]][start[1]][1] == 1 and (x, y) not in answer:
#                         answer.append((x, y))
            

#         bfs(0, 0, (0, 0), heights[0][0])
#         print(answer)
#         return answer
