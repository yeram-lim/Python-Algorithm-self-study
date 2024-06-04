n = int(input())

count = 0
while True:
    if n % 5 == 0:
        count += (n // 5)
        break
    else:
        if n < 5:
            if n % 2 > 0:
                count = -1
                break
            else:
                count += (n // 2)
                break
        
        if n // 5 > 1:
            n -= 5
            count += 1
        else:
            if n % 2 > 0:
                n -= 5
                count += 1
            else:
                count += (n // 2)
                break

print(count)