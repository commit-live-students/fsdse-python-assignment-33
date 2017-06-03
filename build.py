def solution(dic):
    count = 0
    for  str in dic:
        if (str[0] == str[len(str)-1]):
            count += 1
    return count

str = ['abc', 'xyz', 'aba', '1221','abced','123121211']
print solution(str)
