from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        answer = []
        direction_x = [-1, 0, 1, 0]
        direction_y = [0, -1, 0, 1]
        x_length = len(heights)
        y_length = len(heights[0])

        # 0번째에 pacific 갔는지 유무 저장
        # 1번째에 atlantic 갔는지 유부 저장
        visited = [[0 for i in range(y_length)] for i in range(x_length)]
        can_approach_water = [[[0, 0] for i in range(y_length)] for i in range(x_length)]
        
        # 바다 방향 확인
        def bfs(x, y, start, start_height):
            nonlocal can_approach_water
            nonlocal visited
            # if x == start[0] and y == start[1]:
            visited[x][y] = 1

            for i in range(4):
                dx = x + direction_x[i]
                dy = y + direction_y[i]

                if not (dx < 0 or dx > x_length - 1 or dy < 0 or dy > y_length - 1):
                    if visited[dx][dy] != 1:
                        curr_height = start_height
                        next_height = heights[dx][dy]
                        if curr_height >= next_height:
                            # a=''
                            bfs(dx, dy, start, next_height)
                        else:
                            bfs(dx, dy, (dx, dy), next_height)

                else:
                    if dx < 0 or dy < 0:
                        can_approach_water[start[0]][start[1]][0] = 1
                    else:
                        can_approach_water[start[0]][start[1]][1] = 1
                    if can_approach_water[start[0]][start[1]][0] == 1 and can_approach_water[start[0]][start[1]][1] == 1 and (x, y) not in answer:
                        answer.append((x, y))
            

        bfs(0, 0, (0, 0), heights[0][0])
        print(answer)
        return answer

a = Solution()
# b = a.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
b = a.pacificAtlantic([[1,2,2],[3,2,3],[2,4,5]])