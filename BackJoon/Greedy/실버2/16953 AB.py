A, B = map(int, input().split())

count = 1
while True:
  if B < A:
    count = -1
    break
  elif B == A:
    break
  
  if B % 2 == 0:
    B = int(B / 2)
  else:
    if int(str(B)[-1]) == 1:
      B = int(str(B)[0 : -1])
    else:
      B = -1
  count += 1
print(count)