# 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    start = 1
    end = n * max(times)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for t in times:
            total += mid // t
            if total >= n:
                break
        if total >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer