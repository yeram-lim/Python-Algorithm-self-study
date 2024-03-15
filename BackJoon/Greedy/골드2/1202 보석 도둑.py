N, K = list(map(int, input().split()))
j_infos = [[] for i in range(1000000)] 
bag_infos = []
for i in range(N):
    j_weight, j_cost = list(map(int, input().split()))
    j_infos[j_weight].append(j_cost) 
print(j_infos)
# for i in range(K):
#     bag_infos.append(int(input()))
# print(j_infos, bag_infos)
# 3 2
# 1 65
# 5 23
# 2 99
# 10
# 2
# 답 164

# 이런걸 완전 탐색이라고 하나? ㅎ 당연 실패
# N, K = list(map(int, input().split()))
# j_infos = [] # [무제, 가격]을 원소로 하는 보석 정보를 담음
# bag_infos = []
# for i in range(N):
#     j_infos.append(list(map(int, input().split())))
# for i in range(K):
#     bag_infos.append(int(input()))

# # 가격 높은 순으로 정렬
# j_infos.sort(key=lambda x : -x[1])
# bag_infos.sort(reverse=True)

# answer = 0
# j_index = 0
# b_index = 0
# while b_index < K :
#     if j_index >= N:
#         break
#     bag_max = bag_infos[b_index]
#     weight, cost = j_infos[j_index]
#     if weight > bag_max:
#         j_index += 1
#     else:
#         answer += cost
#         j_index += 1
#         b_index += 1

# print(answer)
