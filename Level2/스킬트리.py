def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        i = 0
        for s in skill_tree:
            if s not in skill:
                continue
            if s == skill[i]:
                i += 1
            else:
                break
        else:
            answer += 1
    return answer