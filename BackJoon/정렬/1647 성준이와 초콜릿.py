from collections import defaultdict
import sys
input = sys.stdin.readline

def get_safe_zone(key, t, n):
  effect = 0
  if n > 0:
    if key == 'Chocolate':
      effect = 8 * n - t / 12
    else:
      effect = 2 * n - t * t / 79
  if effect < 0:
    effect = 0
  return effect

eat_timeline = defaultdict(list)
Queries = []
while True:
  info = input().split()
  if info:
    key = info[0]
    t = int(info[1])
    if key == 'Query':
      Queries.append(t)
    else:
      n = info[2]
      eat_timeline[t].append((key, float(n)))
  else:
    break
eat_timeline_keys = sorted(eat_timeline.keys())
print(eat_timeline, Queries, eat_timeline_keys)
# {1: [('Chocolate', 1.0)], 3: [('Coffee', 1.5)]}) [0, 2, 3, 10] [1, 3]

timeline_keys_index = 0
accumulated_chocolate = 0
accumulated_coffee = 0
for query in Queries:
  while True and timeline_keys_index < len(eat_timeline_keys):
    eat_t = eat_timeline_keys[timeline_keys_index]
    if eat_t > query:
      break
    
    for eat in eat_timeline[eat_t]:
      key, n = eat
      if key == 'Chocolate':
        accumulated_chocolate += n
      else:
        accumulated_coffee += n

    timeline_keys_index += 1
  
  chocolate_safe_zone = get_safe_zone('Chocolate', query, accumulated_chocolate)
  coffee_safe_zone = get_safe_zone('Coffee', query, accumulated_coffee)
  safe_zone = chocolate_safe_zone + coffee_safe_zone
  print('-----')
  print(query,accumulated_chocolate,chocolate_safe_zone,'/',accumulated_coffee,coffee_safe_zone)
  print(query, round(safe_zone if safe_zone > 1 else 1.0, 1))
# -----
# 0 0 0 / 0 0
# 0 1.0
# -----
# 2 1.0 7.833333333333333 / 0 0
# 2 7.8
# -----
# 3 1.0 7.75 / 1.5 2.8860759493670884
# 3 10.6
# -----
# 10 1.0 7.166666666666667 / 1.5 1.7341772151898733
# 10 8.9