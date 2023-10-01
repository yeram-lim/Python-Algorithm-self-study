def solution(numbers, target):
    answer = 0
    
    def calculation(num, curr_index):
        nonlocal answer
        if curr_index < len(numbers):
            result1 = num + numbers[curr_index]
            calculation(result1, curr_index + 1)
        
            result2 = num - numbers[curr_index]
            calculation(result2, curr_index + 1)
        else:
            if num == target:
                answer += 1
            return
        
    calculation(0, 0)
    
    return answer

solution([1, 1, 1, 1, 1],	3)