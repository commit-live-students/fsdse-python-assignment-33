def solution(dic):
    count = 0
    for string in dic:
        if string[0]==string[-1]:
            count+=1
        else:
            pass
    return count
