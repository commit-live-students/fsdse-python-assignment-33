def solution(dic):
    count=0
    for i in range(len(dic)):
        if(len(dic[i])>2):
            if(dic[i][0]==dic[i][len(dic[i])-1]):
                count+=1
    return count
print solution(['abc', 'xyz', 'aba', '1221'])
