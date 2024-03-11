from collections import deque
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)
        table = [[INF] * (n + 1) for i in range(n + 1)] #* (n + 1)

        # 최단 경로를 담은 테이블 구함
        for time_info in times:
            start, end, distance = time_info
            if table[start][end] > distance:
                table[start][end] = distance
        
        # print(table)
        # [[1000000000, 1000000000, 1000000000, 1000000000, 1000000000], 
        # [1000000000, 1000000000, 1000000000, 1000000000, 1000000000], 
        # [1000000000, 1, 1000000000, 1, 1000000000], 
        # [1000000000, 1000000000, 1000000000, 1000000000, 1], 
        # [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]]

        total_cost = 0
        visited_count = 0
        visited = [0] * (n + 1)
        q = deque()
        for i in range(1, n + 1): #1 -> 3
            if i == k or i == 0:
                continue
            
            q.append((k, i)) #2,1 -> 2,3
            temp_cost = 0
            while q:
                start, end = q.popleft() #2,1 -> 2,3 -> 3,4
                print('🐻',start, end, visited)
                if table[start][end] < INF:
                    temp_cost += table[start][end]
                    if not visited[end]:
                        visited[end] = 1
                        visited_count += 1
                        for j in range(1, n + 1):
                            if j != k and table[end][j] < INF:
                                q.append((end, j))
                    print('temp_cost',temp_cost, 'q', q, visited, visited_count)
    
            if temp_cost > total_cost:
                total_cost = temp_cost 
        
        return (total_cost if visited_count == (n - 1) else -1)
            


a = Solution()
# b=a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
b=a.networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3,1)
# b=a.networkDelayTime([[1,2,1],[2,1,3]],  2,2)
print(b)