# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

def compare(word, target):
    count = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            count += 1
            if count > 1:
                return False
    return True

def dfs(now, target, words, n):
    if now == target:
        global answer
        answer = min(answer, n)
        return
    for word in words:
        if not compare(now, word):
            continue
        words.remove(word)
        dfs(word, target, words, n + 1)
        words.append(word)

def solution(begin, target, words):
    if target not in words:
        return 0
    global answer
    answer = 50
    dfs(begin, target, words, 0)
    return answer