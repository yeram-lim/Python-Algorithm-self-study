from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict()
    for clothes_pair in clothes:
        if clothes_pair[1] in clothes_dict.keys():
            clothes_dict[clothes_pair[1]].append(clothes_pair[0])
        else:
            clothes_dict[clothes_pair[1]] = [0, clothes_pair[0]]

    for clothes_list in list(clothes_dict.values()):
        answer *= len(clothes_list)

    return answer - 1

print('답:',solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print('답:',solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
