S, C = list(map(int, input().split()))
pa_lengths = []
for i in range(S):
    pa_lengths.append(int(input()))
pa_lengths.sort()

min_pa = pa_lengths[-1] / C
max_pa = pa_lengths[0]
if sum(pa_lengths) / C < pa_lengths[0]: #소숫점 주의, 한 파닭에 들어갈 수 있는 최대 파의 길이
    max_pa = sum(pa_lengths) // C
# print('min_pa:',min_pa,'max_pa:',max_pa)
use_pa_len = 0
while True:
    def get_pa_dak_count(pa_lengths, target_pa):
        pa_dak_count = 0
        for pa in pa_lengths:
            pa_dak_count += pa // target_pa
        return pa_dak_count
    
    pa_dak_count_with_max = get_pa_dak_count(pa_lengths, max_pa)
    if pa_dak_count_with_max == C:
        break

    # if max_pa - min_pa <= 1:
    #     pa_dak_count = get_pa_dak_count(pa_lengths, max_pa)
    #     if pa_dak_count == C:
    #         use_pa_len = max_pa
    #     break

    mid_pa = (min_pa + max_pa) // 2
    pa_dak_count = get_pa_dak_count(pa_lengths, mid_pa)
    
    if pa_dak_count == C:
        min_pa = mid_pa
        if use_pa_len < mid_pa:
            use_pa_len = mid_pa
    if pa_dak_count < C:
        max_pa = mid_pa
    if pa_dak_count > C:
        min_pa = mid_pa
print(int(sum(pa_lengths) - (use_pa_len * C)))


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