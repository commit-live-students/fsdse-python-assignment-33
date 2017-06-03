def solution(dic):
    '''
    Enter your code here
    '''
    count = 0
    for i in dic:
        if(len(i)>2 and i[0] == i[len(i)-1]):
            count = count+1;
    return count

#print(solution(['abc', 'xyz', 'aba', '1221']))
