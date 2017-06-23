def solution(dic):
    '''
    Enter your code here
    '''
    count=0
    for i in dic:
        if i[0]==i[-1]:
            count+=1
        else:
            count+=0
    return count
