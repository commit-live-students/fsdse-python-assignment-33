def solution(dic):
    count = 0
    for each in dic:
        if each[0] == each[-1]:
            count +=1
    return count
