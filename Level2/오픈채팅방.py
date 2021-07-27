def solution(record):
    answer = []
    message = []
    name = {}
    for r in record:
        s = r.split()
        if s[0] == 'Enter':
            message.append(('E', s[1]))
            name[s[1]] = s[2]
        elif s[0] == 'Leave':
            message.append(('L', s[1]))
        else:
            name[s[1]] = s[2]
    for m in message:
        if m[0] == 'E':
            answer.append("{0}님이 들어왔습니다.".format(name[m[1]]))
        else:
            answer.append("{0}님이 나갔습니다.".format(name[m[1]]))

    return answer