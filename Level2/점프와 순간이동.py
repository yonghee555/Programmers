def solution(n):
    ans = 0
    
    if n == 1:
        return 1
    ans += solution(n // 2)
    ans += n % 2
    return ans

print(solution(5))
print(solution(6))
print(solution(5000))