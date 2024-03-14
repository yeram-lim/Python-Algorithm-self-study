N = int(input())
words = [] #['ACDEB', 'GCF']
letter_index = {} #{'G': 3, 'C': 4, 'F': 1, 'A': 5, 'D': 3, 'E': 2, 'B': 1}
for i in range(N):
    word = input()
    words.append(word)
    for j in range(len(word)):
        letter = word[j]
        # 각 문자의 최대 자릿수를 저장
        if letter_index.get(letter):
            if letter_index[letter] < len(word) - j:
                letter_index[letter] = (len(word) - j)
        else:
            letter_index[letter] = (len(word) - j)

# value(각 알파벳의 최대자릿수)로 정렬
# [('A', 5), ('C', 4), ('G', 3), ('D', 3), ('E', 2), ('F', 1), ('B', 1)]
sorted_dict_list = sorted(letter_index.items(), key = lambda item: item[1], reverse=True)

# 자릿수가 큰 만큼 큰 수를 부여
# {'G': 7, 'C': 8, 'F': 4, 'A': 9, 'D': 6, 'E': 5, 'B': 3}
num_count = 9
for index_info in sorted_dict_list:
    letter, index = index_info
    letter_index[letter] = num_count
    num_count -= 1


answer = 0
for word in words:
    num_string = ''
    for letter in word:
        num_string += str(letter_index[letter])
    answer += int(num_string)
print(answer)


# 2
# GCF
# ACDEB
# 답 99437

# 2
# AAA
# AAA
# 답 1998