import math


def get_minutes(time_stirng):
  [hour, minute] = time_stirng.split(':')
  return int(hour) * 60 + int(minute)

def calculate_parking_fee(fee_info, parking_duration):
  [basic_duration, basic_fee, unit_duration, unit_fee] = fee_info
  total_fee = basic_fee
  parking_duration -= basic_duration
  if parking_duration > 0:
    total_fee += math.ceil(parking_duration / unit_duration) * unit_fee
  
  return total_fee

def solution(fees, records):
    answer = []
    info = {}
    max_time = '23:59'
    
    for record in records:
      [time, car_number, type] = record.split(' ')
      car_number = int(car_number)
      if info.get(car_number):
        info[car_number].append(time)
      else:
        info[car_number] = [time]
    
    sorted_car_list = sorted(info.keys())
    for car_number in sorted_car_list:
      car_records = info[car_number]
      total_duration = 0
      total_fee = 0
      for i in range(0, len(car_records), 2):
        in_time = car_records[i]
        out_time = car_records[i + 1] if i < len(car_records) - 1 else max_time
        total_duration += get_minutes(out_time) - get_minutes(in_time)
      total_fee = calculate_parking_fee(fees, total_duration)
      answer.append(total_fee)
    
    return answer
  
# print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# print(solution([1, 461, 1, 10],["00:00 1234 IN"])) 