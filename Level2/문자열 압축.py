def solution(s):
    unit_size = len(s) // 2
    size = len(s)
    compressed = [size]
    while unit_size > 0:
        i = 0
        count = 1
        compressed_length = 0
        while i + 2 * unit_size <= size:
            if s[i:i + unit_size] == s[i + unit_size:i + 2 * unit_size]: #다음에 나올 문자열과 같으면 count를 하나 더해줌
                count += 1
            elif count != 1: # s[i:i + unit_size] 문자열까지 총 count개만큼 같았으므로 이를 이용하여 길이를 세어줌
                compressed_length += len(str(count)) + unit_size
                count = 1
            else: # 앞의 문자열과도 다르고 뒤의 문자열과도 다른 경우
                compressed_length += unit_size
            i += unit_size
        if count != 1: # 마지막 unit_size + (size % unit_size)만큼의 길이에 대해서 세어 줌
            compressed_length += len(str(count)) + unit_size + len(s[i + unit_size:])
        else:
            compressed_length += len(s[i:])
        compressed.append(compressed_length)
        unit_size -= 1
    
    answer = min(compressed)
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))