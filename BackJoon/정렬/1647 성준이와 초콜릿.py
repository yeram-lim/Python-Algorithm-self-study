import sys
input = sys.stdin.readline

def get_chocolate_safe_zone(t, n):
  return 8 * n - t / 12

def get_coffee_safe_zone(t, n):
  return 2 * n - t * t / 79

timeline = {}
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
      timeline[t] = (key, float(n))
  else:
    break

timeline_keys = sorted(timeline.keys())
print(timeline, Queries,timeline_keys)
timeline_keys_index = 0
accumulated_chocolate = 0
accumulated_coffee = 0
for query in Queries:
  while True and timeline_keys_index < len(timeline_keys):
    target_t = timeline_keys[timeline_keys_index]
    if target_t > query:
      break
    
    key, n = timeline[target_t]
    
    if key == 'Chocolate':
      accumulated_chocolate += n
    else:
      accumulated_coffee += n
    timeline_keys_index += 1
  
  chocolate_safe_zone = get_chocolate_safe_zone(query, accumulated_chocolate) if accumulated_chocolate > 0 else 0 
  coffee_safe_zone = get_coffee_safe_zone(query, accumulated_coffee) if accumulated_coffee > 0 else 0
  safe_zone = chocolate_safe_zone + coffee_safe_zone
  print('-----')
  print(query,accumulated_chocolate,chocolate_safe_zone,'/',accumulated_coffee,coffee_safe_zone)
  print(query, round(safe_zone if safe_zone > 1 else 1.0, 1))
