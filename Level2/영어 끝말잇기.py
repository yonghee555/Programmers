def solution(n, words):
    words_used = []
    
    for i, word in enumerate(words):
        if i == 0:
            words_used.append(word)
            continue
        if word[0] != words_used[-1][-1] or word in words_used:
            return [i % n + 1, i // n + 1]
        else:
            words_used.append(word)
    
    return [0, 0]