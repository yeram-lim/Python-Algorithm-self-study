N = int(input())
count = 0
answer = 1
while N > 0:
    # print(N, answer)
    if answer > N:
        answer = (answer + N)
        N = 0
    else:
        N -= answer
        answer += 1
        count += 1
print(count)