'''
# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.


**Notes:**

* Define a function to accept a list as parameter.
* Iterate over each element and verify if first char and last char are same.
* If same increment count by one.
* Return count.


**Instructions:**
* Program should be written in file build.py
* Function name should be solution.
* Input

       Type:  List
       Value: ['abc', 'xyz', 'aba', '1221']

* Expected Output

        Type:  Integer
        Value: 2

'''
def solution(dic):
    count = 0
    for val in dic:
        if val[0] == val[-1]:
            count +=1
    return count
