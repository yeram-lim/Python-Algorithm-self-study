from collections import Counter


name = input()
result = "I'm Sorry Hansoo"

# 각 알파벳을 key로 value에는 개수를 가지고 있는 딕셔너리
alphabet_count_dict = Counter(name)

alphabets = list(alphabet_count_dict.keys())
# 알파벳의 종류가 하나이면 그 자체로 팰린드롬
if len(alphabets) == 1:
    result = name
else:
    canMakePalindrome = True
    odd_alphabet = '' # 개수가 홀수 알파벳
    for alphabet in alphabets:
        if alphabet_count_dict[alphabet] % 2 != 0:
            # 개수가 홀수 알파벳이 이미 저장되어 있다면 개수가 홀수 알파벳이 여러개이므로 팰린드롬을 만들 수 없음
            if odd_alphabet != '':
                canMakePalindrome = False
                break
            # 개수가 홀수 알파벳 저장
            else:
                odd_alphabet = alphabet
                
    if canMakePalindrome:
        alphabets.sort()
        result = ''
        # 돌아가면서 알파벳들의 개수의 절반만큼 result에 알파벳을 넣음
        for alphabet in alphabets:
            result += alphabet * (alphabet_count_dict[alphabet] // 2)

        # 지금까지 result에 저장된 문자열을 거꾸로 만들어줌
        reverse = result[::-1]
        # 개수가 홀수 알파벳이 있었다면 마지막에 더해줌
        result += odd_alphabet 
        result += reverse
print(result)