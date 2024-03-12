N = int(input())
distance_list = list(map(int, input().split()))
city_list = list(map(int, input().split()))

oil = 0
cost = 0

for i in range(N):
    if oil > 0:
        oil -= distance_list[i - 1]
    if oil == 0:
        curr_city = city_list[i]
        for j in range(i + 1, N):
            next_city = city_list[j]
            distance = distance_list[j - 1]
            oil += distance
            cost += curr_city * distance
            if curr_city > next_city:
                break
print(cost)
# 4
# 2 3 1
# 5 2 4 1
# 답 18

# 4
# 3 3 4
# 1 1 1 1
# 답 10