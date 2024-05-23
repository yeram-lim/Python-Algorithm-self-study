T = int(input())
results = []
for i in range(T):
    count = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    result = 0
    for a in A:
        pointer_start, pointer_mid, pointer_end = 0, 0, len(B) - 1
        
        while pointer_start < pointer_end:
            pointer_mid = (pointer_end - pointer_start) // 2
            b_start, b_mid, b_end = B[pointer_start], B[pointer_mid], B[pointer_end]

            if pointer_start == pointer_mid:
                result += pointer_mid
                break

            if b_mid > a:
                pointer_end = pointer_mid
            if b_mid < a:
                pointer_start = pointer_mid
            

            # if b_start > a:
            #     break
            # elif b_end < a:
            #     result += pointer_end + 1
            #     break
            # elif b_start == a:
            #     result += pointer_start
            #     break
            # elif b_end == a:
            #     result = pointer_end
            #     break
            # elif b_mid == a:
            #     result += pointer_mid
            #     break
            # else:
            #     if pointer_mid == pointer_start:
            #         if a > b_start:
            #             result += pointer_start + 1
            #         break
            #     if b_mid > a:
            #         pointer_end = pointer_mid
            #     if b_mid < a:
            #         pointer_start = pointer_mid
    results.append(result)

for result in results:
    print(result)


# 1
# 3 4
# 2 13 7
# 103 11 290 215

# 2 7 13 - 11 103 215 290

# 1
# 5 3
# 8 1 7 3 1
# 3 6 1

# 11378 - 136

# 2
# 5 3
# 8 1 7 3 1
# 3 6 1
# 3 4
# 2 13 7
# 103 11 290 215