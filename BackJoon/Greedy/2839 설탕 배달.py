N = int(input())

kg_list = [5, 3]
answer = 0

def get_count(total_kg, kg):
    count = total_kg // kg
    last = total_kg % kg
    return [count, last]

temp_count = 0
temp_last = 0
for kg in kg_list:
    total = N
    if temp_last > 0 and temp_last % kg == 0:
        total = temp_last
    result = get_count(total, kg)
    count, last = result
    
    if total != N:
        temp_count += count
    else:
        temp_count = count if count < temp_count else temp_count
    temp_last = last
    
print(temp_count if temp_last == 0 else -1)