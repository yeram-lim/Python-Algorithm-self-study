name = input()
result = "I'm Sorry Hansoo"

alphabet_count_dict = {}
for i in range(len(name)):
    if alphabet_count_dict.get(name[i]):
        alphabet_count_dict[name[i]] += 1
    else:
        alphabet_count_dict[name[i]] = 1

alphabets = list(alphabet_count_dict.keys())
if len(alphabets) == 1:
    result = name
else:
    isPalindrome = True
    odd_alphabet = ''
    for alphabet in alphabets:
        if alphabet_count_dict[alphabet] % 2 != 0:
            if odd_alphabet != '':
                isPalindrome = False
                break
            else:
                odd_alphabet = alphabet
    if isPalindrome:
        alphabets.sort()
        result = ''
        for alphabet in alphabets:
            if alphabet != odd_alphabet:
                result += alphabet * (alphabet_count_dict[alphabet] // 2)
        reverse = result[::-1]
        result += odd_alphabet * (alphabet_count_dict[alphabet])
        result += reverse
    print(result)

# AABCBAA