def solution(dic):
    count = 0
    for a in dic:
        if a[0] == a[len(a) - 1] and a[1] == a[len(a) - 2]:
            count = count + 1

    return count
