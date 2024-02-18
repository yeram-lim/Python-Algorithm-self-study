def solution(nums):
    answer = 0
    set_nums = set(nums)
    if len(nums) // 2 < len(set_nums):
      answer = len(nums) // 2
    else:
      answer = len(set_nums)
    return answer


# from itertools import combinations, permutations


# def solution(nums):
#     answer = 0
#     combi_list = list(combinations(nums, len(nums) // 2))
#     #[(3, 1), (3, 2), (3, 3), (1, 2), (1, 3), (2, 3)]
#     print('combi_list',combi_list)
    
#     for combi in combi_list:
#       combi_set = set(combi)
#       if answer < len(combi_set):
#         answer = len(combi_set) 
#         if len(combi_set) == (len(nums) // 2):
#           break
#     return answer
  
# # print(solution([3,3,3,2,2,4]))
# print(solution([3,3,3,2,2,2]))