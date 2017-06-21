def solution(dic):
    '''
    Enter your code here
    '''
    count = 0
    for i in dic:
        if isinstance(i, str) and i[0]==i[len(i)-1]:
            count += 1
    return count
