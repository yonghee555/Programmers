def solution(str1: str, str2: str):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    str1_dict = {}
    str2_dict = {}
    subset = []
    superset = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            if str1[i:i + 2] in str1_dict:
                str1_dict[str1[i:i + 2]] += 1
            else:
                str1_dict[str1[i:i + 2]] = 1

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            if str2[i:i + 2] in str2_dict:
                str2_dict[str2[i:i + 2]] += 1
            else:
                str2_dict[str2[i:i + 2]] = 1

    for i in str1_dict.keys():
        if i in str2_dict:
            subset.append(min(str1_dict[i], str2_dict[i]))
            superset.append(max(str1_dict[i], str2_dict[i]))
        else:
            superset.append(str1_dict[i])
    for i in str2_dict.keys():
        if i not in str1_dict:
            superset.append(str2_dict[i])
    if sum(superset) == 0:
        return 65536
    answer = sum(subset) / sum(superset) * 65536

    return int(answer)
