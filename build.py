def solution(dic):
    '''
    Enter your code here
    '''
    count = 0
    for word in dic:
        if word[0] == word[-1] :
            count += 1
    return count
