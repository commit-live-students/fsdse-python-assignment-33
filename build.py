def solution(dic):
    count = 0

    for i in range (0, len(dic)):
            last_index = len(dic[i])-1
            if last_index >= 2:
                if dic[i][0] == dic[i][last_index]:
                    count += 1

    return count
