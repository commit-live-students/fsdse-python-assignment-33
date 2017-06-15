def solution(list):
    count = 0
    for k in list:
        if len(k) >= 2 and k[0]==k[-1]:
            count = count+1
    return count

output=solution(['abc', 'xyzx', 'aba', '1221'])
print output
