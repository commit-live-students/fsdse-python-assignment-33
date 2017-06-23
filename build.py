def solution(dic):
    count = 0
    for elem in dic:
    #     print elem[0], elem[len(elem)-1]
    #     for elem1 in elem:
        if (elem[0] == elem[len(elem)-1]):
            count += 1
    return count
