import sys
input = sys.stdin.readline

S, C = list(map(int, input().split()))
pa_list = []
for i in range(S):
    pa_list.append(int(input()))

min_pa = pa_list[-1] / C
max_pa = pa_list[0]
if sum(pa_list) / C < pa_list[0]: #소숫점 주의, 한 파닭에 들어갈 수 있는 최대 파의 길이
    max_pa = sum(pa_list) // C

while min_pa <= max_pa:
    mid_pa = (min_pa + max_pa) // 2
    pa_dak_count = 0
    for pa in pa_list:
        pa_dak_count += pa // mid_pa

    if pa_dak_count < C:
        max_pa = mid_pa - 1
    if pa_dak_count >= C:
        min_pa = mid_pa + 1
print(int(sum(pa_list) - (max_pa * C)))


# 3 5
# 440
# 350
# 230 
# 사용하는 파 길이 : 175
# 답 : 145

# 3 3
# 10
# 11
# 13
# 7
# 사용하는 파 길이 : 10
# 답 : 4