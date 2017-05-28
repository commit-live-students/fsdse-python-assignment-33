def solution(dic):
    '''
    Enter your code here
    '''
    count = 0
    for listValue in dic:
        print listValue
        for charCatch in range(0,len(listValue)):
            if (listValue[0] == listValue[len(listValue)-1]):
                count = count + 1
                break

    return count

solution(['abc', 'xyz', 'aba', '1221'])
