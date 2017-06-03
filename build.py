def solution(_list):
    '''
    Enter your code here
    '''
    count = len([string for string in _list if len(string) >=2 and string[0]==string[-1]])
    return count
