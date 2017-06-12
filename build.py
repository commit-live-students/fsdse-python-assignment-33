def solution(dic):
    count = 0
    for lValue in dic:
#       print lValue
        for charCatch in range(0,len(lValue)):
            if (lValue[0] == lValue[len(lValue)-1]):
                count = count + 1
                break
#        print charCatch
    print count
    return count

solution(['abc', 'xyz', 'aba', '1221'])
