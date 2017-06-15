def solution(dic):
    count = 0

    for i in dic:
        if i[0] == i[len(i)-1]:
            count += 1
    #print count
    return count

#dic = ['abc', 'xyz', 'aba', '1221']
#solution(dic)
