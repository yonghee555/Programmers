# 다단계 칫솔 판매
# https://programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    enroll_dict = {}
    answer_dict = {}
    for i, e in enumerate(enroll):
        enroll_dict[e] = referral[i]
        answer_dict[e] = 0
    for i in range(len(seller)):
        sel = seller[i]
        ref = enroll_dict[sel]
        a = amount[i] * 100
        while True:
            if ref == '-':
                answer_dict[sel] += a - int(a * 0.1)
                break
            commission = int(a * 0.1)
            answer_dict[sel] += a - commission
            if commission == 0:
                break
            a = commission
            sel, ref = ref, enroll_dict[ref]
    answer = list(answer_dict.values())
    return answer