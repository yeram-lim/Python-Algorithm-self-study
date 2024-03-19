import heapq

def dijkstra(dist,adj):
    # 출발노드를 기준으로 각 노드들의 최소비용 탐색
    heap = []
    heapq.heappush(heap, [0,1])  # 거리,노드
    while heap:
        cost, node = heapq.heappop(heap)
        for c,n in adj[node]:
            if cost+c < dist[n]:
                dist[n] = cost+c
                heapq.heappush(heap, [cost+c,n])


def solution(N, road, K):
    dist = [float('inf')]*(N+1)  # dist 배열 만들고 최소거리 갱신할거임
    dist[1] = 0  # 1번은 자기자신이니까 거리 0
    adj = [[] for _ in range(N+1)]  # 인접노드&거리 기록할 배열
    for r in road:
        adj[r[0]].append([r[2],r[1]]) # 거리, 도착 노드
        adj[r[1]].append([r[2],r[0]])
    print('adj',adj) 
    # [[], [[1, 2], [2, 4]], [[1, 1], [3, 3], [2, 5]], [[3, 2], [1, 5]], [[2, 1], [2, 5]], [[2, 2], [1, 3], [2, 4]]]
    dijkstra(dist,adj)
    return len([i for i in dist if i <=K])
a = solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)

# # 5
# # [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# # 3
# # result = 4

# import heapq


# def solution(N, road, K):
#     answer = 0
#     links = [[] for i in range(N + 1)]
#     distances = [-1 for i in range(N + 1)]
#     for road_i in road:
#         start, end, distance = road_i
#         links[start].append((distance, end))
#     # [[], [(1, 2), (2, 4)], [(3, 3)], [], [], [(2, 2), (1, 3), (2, 4)]]
    
#     heap = []
#     for i in range(1, N + 1):
#         link_nodes = links[i]
#         for link in link_nodes:
#             heapq.heappush(heap, link)
#     print(links)

#     return answer
