def solution(n):
    a = n ** (0.5)
    if a % 1 == 0: return (a + 1) ** 2
    else: return -1