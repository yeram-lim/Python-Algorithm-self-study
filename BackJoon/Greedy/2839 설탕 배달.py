N = int(input())

kg_list = [5, 3]
answer = 0

if N % 5 == 0:
    print(N // 5)
else:
    total = N
    count = 0
    while total > 0:
        total -= 3
        count += 1

        if total % 5 == 0:
            count += total // 5
            print(count)
            break
        elif total < 3:
            print(-1)
            break
        elif total == 0:
            print(count)
            break