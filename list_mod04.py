def remove_positive(lst):
    '''Given a list of numbers, write a function that returns a new list where all the positive numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without positive numbers.
    '''
    list1=[]
    for i in range(len(lst)):
        if lst[i]<0:
            list1.append(lst[i])
    return list1
print(remove_positive([1,2,-3,4,4,6,7,-7,8]))