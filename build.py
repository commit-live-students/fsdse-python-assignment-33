def solution(dic):
    '''
    Enter your code here
    '''
    count = 0
    for i in dic:
        if i[0] == i[-1]:
            count+=1
    return count

dic =  ['abc', 'xyz', 'aba', '1221']
print(solution(dic))
