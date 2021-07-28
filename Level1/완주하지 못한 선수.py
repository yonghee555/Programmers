def solution(participant, completion):

    runners = {}
    for c in completion:
        if c not in runners:
            runners[c] = 1
        else:
            runners[c] += 1
    for p in participant:
        if p not in runners:
            return p
        elif runners[p] == 0:
            return p
        else:
            runners[p] -= 1
