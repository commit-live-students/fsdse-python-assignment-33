def solution(dic):
    '''
    Enter your code here
    '''
    count = 0
    for element in dic:
        if element[0] == element[-1]:
            count += 1
        else:
            pass
    return count
