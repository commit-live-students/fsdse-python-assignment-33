def solution(dic):
    count=0
    for i in dic:
        if len(i)>2:
            if i[0]==i[-1]:
                count+=1
    print count
    return count
solution(['abc', 'xyz', 'aba', '1221'])
