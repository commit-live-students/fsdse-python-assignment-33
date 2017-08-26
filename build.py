def solution(dic):
    count = 0
    for i in dic:
        if i[0] == i[len(i)-1]:
            count += 1
    return count

lis = ['abc', 'xyz', 'aba', '1221']
solution(lis)
