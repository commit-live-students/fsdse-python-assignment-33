def solution(dic):
    c = 0
    for word in dic:
        if word[0] == word[-1]:
            c += 1
    return c
