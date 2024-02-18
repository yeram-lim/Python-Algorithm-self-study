from collections import defaultdict 

def solution(phone_book):
    answer = True
    dict = defaultdict()
    phone_book.sort(key=len)
    for phone_number in phone_book:
      for index in range(len(phone_number)):
        print(dict, phone_number[0 : int(index) + 1])
        if dict.get(str(phone_number[0 : int(index) + 1])):
          answer = False
          break
      dict[phone_number] = True
    return answer

print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123","456","789"]))


# from collections import defaultdict 

# def solution(phone_book):
#     answer = True
#     dict = defaultdict()
#     for number in phone_book:
#         for key in dict.keys():
#             if number.startswith(key) or key.startswith(number):
#                 answer = False
#                 break
#         dict[number] = number
#     return answer