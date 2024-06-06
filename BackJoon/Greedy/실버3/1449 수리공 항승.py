N, L = map(int, input().split())
leak_positions = list(map(int, input().split()))
leak_positions.sort()

# 붙일 테이프의 시작점과 끝점들을 구해준다.
fix_positions = []
for i, position in enumerate(leak_positions):
  start = position - 0.5#, position + 0.5
  if i == 0:
    fix_positions.append(start)
  if i != 0:
    prev_start, prev_end = leak_positions[i - 1] - 0.5, leak_positions[i - 1] + 0.5
    if position - leak_positions[i - 1] > 1:
      fix_positions.append(prev_end)
      fix_positions.append(start)
fix_positions.append(leak_positions[-1] + 0.5)

pointer = 0
count = 0
for i in range(0, len(fix_positions) - 1, 2):
  # 테이프를 붙여야 할 시작과 끝
  start, end = fix_positions[i], fix_positions[i + 1]
  if pointer > start:
    start = pointer
  
  # 시작점과 끝점의 길이
  fix_length = end - start
  required_tape = fix_length // L 
  # 이어붙이는 경우를 고려하더라도 테이프를 붙여야 할 길이보다 고쳐야 할 길이가 길면 테이프를 하나 더 추가
  if fix_length % L > 0:
    required_tape += 1
  count += required_tape
  pointer = start + (L * required_tape)

print(int(count))
# [0.5, 3.5, 4.5, 6.5, 7.5, 8.5]
# 6 2
# 1 2 3 5 6 8