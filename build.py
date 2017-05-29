def solution(dic):
    count = 0
    for rec in dic:

        if(len(rec) >= 2):
            if(rec[:1] == rec[-1:]):
                count = count + 1

    return count

print solution(['abc', 'xyz', 'aba', '1221'])
