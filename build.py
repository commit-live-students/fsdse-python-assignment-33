def solution(dic):
    count=0
    for v in dic:
        if(len(v)>2 and v[0]==v[-1]):
            count = count + 1
    return count
print(solution(['abc', 'xyz', 'aba', '1221']))
