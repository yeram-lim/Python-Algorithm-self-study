N = int(input())

kg_list = [5, 3]
answer = 0

temp_kg1 = N
temp_count1 = 0
for kg in kg_list:
    if temp_kg1 % kg == 0:
        count = temp_kg1 // kg
        last = temp_kg1 % kg
        temp_count1 += count
        N = last

temp_kg2 = N
temp_count2 = 0
for kg in kg_list:
    count = temp_kg2 // kg
    last = temp_kg2 % kg
    temp_count2 += count
    temp_kg2 = last
print(answer if N == 0 else -1)