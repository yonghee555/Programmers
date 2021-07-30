from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        a = {}
        for order in orders:
            if c > len(order):
                continue
            comb = combinations(order, c)
            for cb in comb:
                cb = tuple(sorted(cb))
                if cb not in a:
                    a[cb] = 1
                else:
                    a[cb] += 1
        max = 1
        max_key = []
        for d in a.keys():
            if a[d] > max:
                max = a[d]
                max_key = [d]
            if a[d] == max and a[d] > 1:
                max_key.append(d)
        max_key = set(max_key)
        for m in max_key:
            answer.append(''.join(m))
    return sorted(answer)