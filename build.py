def solution(lis):
    count = 0
    for item in lis:
        if len(item)>=2 and item[0] == item[-1]:
            count +=1
    return count
