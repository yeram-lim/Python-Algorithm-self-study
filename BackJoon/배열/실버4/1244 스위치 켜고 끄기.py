def turn_on_or_off_switch(switches, index):
    if switches[index] == 1:
      switches[index] = 0
    else:
      switches[index] = 1

def turn_switch_by_man(switches, index):
  for i in range(index - 1, len(switches), index):
    turn_on_or_off_switch(switches, i)

def turn_switch_by_woman(switches, index):
  start, end = index - 1, index - 1
  while 0 <= start and end < len(switches) and switches[start] == switches[end]:
    turn_on_or_off_switch(switches, start)
    if start != end:
      turn_on_or_off_switch(switches, end)
    start -= 1
    end += 1

switch_count = int(input())
switches = list(map(int, input().split()))
student_count = int(input())

for i in range(student_count):
  student_info = list(map(int, input().split()))
  if student_info[0] == 1:
    turn_switch_by_man(switches, student_info[1])
  else:
    turn_switch_by_woman(switches, student_info[1])

for k in range(1, switch_count + 1):
    print(switches[k - 1], end = " ")
    if k % 20 == 0:
        print()

# 8
# 0 1 0 1 0 0 0 1
# 2
# 1 4 
# 2 3
  
# 01000000
# 01100000