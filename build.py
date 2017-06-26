def solution(dic):
    count = 0
    for val in dic:
        if val[0] == val[-1]:
            count +=1
    return count
