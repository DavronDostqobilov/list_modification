def remove_max(lst):
    '''Given a list of numbers, write a function that returns a new list where all the maximum numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without maximum numbers.
    '''
    mx=0
    for i in range(len(lst)):
        if mx<lst[i]:
            mx=lst[i]
    lst.pop(lst.index(mx))
    return lst
print(remove_max([1,2,3,4,5,6,7]))