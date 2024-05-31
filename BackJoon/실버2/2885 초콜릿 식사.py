K = int(input())

choco_size = 0
i = 0
while True:
    if K < (1 << i):
        choco_size = 1 << i
        break
    else:
        i += 1
# print(choco_size)

left = choco_size
eat_size = 0
count = 0
while True:
    left = left // 2
    # eat_size += left
    count += 1
    if eat_size + left == K:
        eat_size += left
        break
    elif eat_size + left > K:
        continue
    elif eat_size + left < K:
        eat_size += left
print(choco_size, count)