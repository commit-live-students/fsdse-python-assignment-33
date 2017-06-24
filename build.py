def solution(dic):
    count = 0
    for i in range(0, len(dic)):
        if (dic[i][0] == dic[i][-1]):
            count = count +1
    print count
    return count
