weekday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(a, b):
    day = b
    for i in range(0, a - 1):
        day += day_of_month[i]
    answer = weekday[(day + 4)% 7]
    return answer
