from math import ceil, gcd

def solution(w, h):
    answer = w * h - (w + h - gcd(w, h))
    return answer

# def solution(w, h):
#     answer = w * h
#     a, b = max(w, h), min(w, h)
#     n = ceil(a / b) * b
#     return answer - n
