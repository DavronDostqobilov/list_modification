def remove_min(lst):
    '''Given a list of numbers, write a function that returns a new list where all the minimum numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list wihout minimum numbers.
    '''
    mn=lst[0]
    for i in range(len(lst)):
        if mn>lst[i]:
            mn=lst[i]
    lst.pop(lst.index(mn))
    return lst
print(remove_min([1,2,3,4,5,6,7]))