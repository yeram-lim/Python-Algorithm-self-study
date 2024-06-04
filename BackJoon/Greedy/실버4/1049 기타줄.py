N, M = map(int, input().split())
guitar_six_line_costs = []
guitar_one_line_costs = []
for i in range(M):
    six, one = map(int, input().split())
    guitar_six_line_costs.append(six)
    guitar_one_line_costs.append(one)
min_six_cost = min(guitar_six_line_costs)
min_one_cost = min(guitar_one_line_costs)

print(min(min_six_cost * ((N // 6) + 1), min_six_cost * (N // 6) + min_one_cost * (N % 6), min_one_cost * N))