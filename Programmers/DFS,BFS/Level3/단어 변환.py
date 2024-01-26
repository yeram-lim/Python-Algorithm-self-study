from collections import deque

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    q = deque()
    q.append((begin, 0))

    while q:
        current_word, step = q.pop()

        if current_word == target:
            answer = step
            break

        for word in words:
            diff_letter_count = 0
            if current_word != word:
                for i in range(len(current_word)):
                    if current_word[i] != word[i]:
                        diff_letter_count += 1
                    if diff_letter_count > 1:
                        break
                if diff_letter_count == 1:
                    q.append((word, step + 1))

    return answer