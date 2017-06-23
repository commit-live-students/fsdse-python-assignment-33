def solution(string_list):
    count = 0
    for element in string_list:
        if(element[0] == element[-1]):
            count = count+1
    return count
