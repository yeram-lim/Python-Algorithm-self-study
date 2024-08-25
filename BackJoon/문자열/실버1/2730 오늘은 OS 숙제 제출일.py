T = int(input())

def make_string(day, month, year, diff):
  date = str(month) + '/' + str(day) + '/' + str(year)
  diff_abs = abs(diff)
  day = 'DAY' if diff_abs == 1 else 'DAYS'
  period = 'AFTER' if diff > 0 else 'PRIOR'
  if diff > 7 or diff < -7:
    return 'OUT OF RANGE'
  elif diff == 0:
    return 'SAME DAY'
  else:
    return f"{date} IS {str(diff_abs)} {day} {period}"
  
def is_leap_year(year):
    is_leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        is_leap = True
    return is_leap
  
# 7일이 넘는다면 정확히 며칠인지 구할 필요x
def get_diff_days(prev_d, prev_m, prev_y, after_d, after_m, after_y):
  thirthy_one_months = [1, 3, 5, 7, 8, 10, 12]
  thirthy_months = [4, 6, 9, 11]
  if prev_y == after_y:
    if prev_m == after_m:
      return after_d - prev_d
    elif after_m - prev_m > 2: #두 달 이상 차이나면 무조건 7일 이상 차이 남
      return 8
    else:
      if prev_m in thirthy_months:
        return (30 - prev_d) + after_d
      elif prev_m in thirthy_one_months:
        return (31 - prev_d) + after_d
      else: # 2월인 경우
        Feb_days = 29 if is_leap_year(prev_y) else 28
        return (Feb_days - prev_d) + after_d
  elif after_y - prev_y > 2 or not (prev_m == 12 and after_m == 1): # 두 달 이상 차이나면 무조건 7일 이상 차이 남
    return 8
  else:
    return (31 - prev_d) + after_d
    

infos = []
for i in range(T):
  info = input()
  deadline, submit_date = info.split(' ')
  deadline_m, deadline_d, deadline_y = map(int, deadline.split('/'))
  submit_m, submit_d = map(int, submit_date.split('/'))
  
  # 일단 할당
  d, m, y = submit_d, submit_m, deadline_y
  # print(deadline_d, deadline_m, deadline_y,'|',d, m, y)
  is_submit_after = False
  if deadline_m == 1:
    if submit_m == 12:
      y = deadline_y - 1
    elif submit_m > 1:
      is_submit_after = True
      
  elif deadline_m == 12:
    if submit_m == 1:
      y = deadline_y + 1
      is_submit_after = True
      
  elif deadline_m < submit_m:
      is_submit_after = True
      
  elif deadline_m == submit_m:
      if deadline_d < submit_d:
        is_submit_after = True
  
  diff_days = 0
  if is_submit_after:
    diff_days = get_diff_days(deadline_d, deadline_m, deadline_y, d, m, y)
  else:
    diff_days = -1 * get_diff_days(d, m, y, deadline_d, deadline_m, deadline_y)
    
  print(make_string(d, m, y, diff_days))