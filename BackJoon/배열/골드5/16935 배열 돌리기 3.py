# 1번 연산, 2번 연산 가능
def reverse_elements(A):
  a = []
  for i in range(len(A) - 1, -1, -1):
    a.append(A[i])
  return a

def rotate_90_to_right(A):
  a = [[] for _ in range(len(A[0]))]
  for i in range(len(A)):
    for j in range(len(A[i])):
      a[j].insert(0, A[i][j])
  return a

def rotate_90_to_left(A):
  a = [[] for _ in range(len(A[0]))]
  for i in range(len(A)):
    for j in range(len(A[i])):
      a[len(A[i]) - 1 - j].append(A[i][j])
  return a

def rotate_group_90_to_right(A):
  half_index_of_col = int(len(A) / 2)
  half_index_of_row = int(len(A[0]) / 2)
  a = [[] for _ in range(len(A))]
  for i in range(len(A)):
    is_top_group = i < half_index_of_col
    if is_top_group:
      a[i] += A[i][:half_index_of_row]
      a[i + half_index_of_col] += A[i][half_index_of_row:]
    else:
      a[i - half_index_of_col] = A[i][:half_index_of_row] + a[i - half_index_of_col]
      a[i] =  A[i][half_index_of_row:] + a[i]
  return a
      
def rotate_group_90_to_left(A):
  half_index_of_col = int(len(A) / 2)
  half_index_of_row = int(len(A[0]) / 2)
  a = [[] for _ in range(len(A))]
  for i in range(len(A)):
    is_top_group = i < half_index_of_col
    if is_top_group:
      a[i + half_index_of_col] += A[i][:half_index_of_row]
      a[i] += A[i][half_index_of_row:]
    else:
      a[i] += A[i][:half_index_of_row]
      a[i - half_index_of_col] +=  A[i][half_index_of_row:]
  return a
  
N, M, R = list(map(int, input().split()))
A = []
for i in range(N):
  A.append(list(map(int, input().split())))
calculations = list(map(int, input().split()))

for calculation in calculations:
  if calculation == 1:
    A = reverse_elements(A)
  elif calculation == 2:
    a = []
    for i in A:
      a.append(reverse_elements(i))
    A = a
  elif calculation == 3:
    A = rotate_90_to_right(A)
  elif calculation == 4:
    A = rotate_90_to_left(A)
  elif calculation == 5:
    A = rotate_group_90_to_right(A)
  elif calculation == 6:
    A = rotate_group_90_to_left(A)

for element in A:
  print(*element)