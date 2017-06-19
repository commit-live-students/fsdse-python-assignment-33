def solution(lst):
    count = 0
    for e in lst:
        if e[0] == e[len(e)-1]:
            count+=1
    return count

t = solution(['abc','xyz','aba','1221'])
print t
