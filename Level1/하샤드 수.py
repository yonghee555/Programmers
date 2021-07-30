def solution(x):
    x_str = str(x)
    sum_x = 0
    for s in x_str:
        sum_x += int(s)
    answer = True
    if x % sum_x != 0: answer = False
    return answer