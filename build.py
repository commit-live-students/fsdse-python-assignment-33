def solution(dic):
    count = 0

    for word in dic:
      if len(word) > 1 and word[0] == word[-1]:
          count += 1
    return count

print(solution(['abc', 'xyz', 'aba', '1221']))
