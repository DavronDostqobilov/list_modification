def remove_odd(lst):
    '''Given a list of numbers, write a function that returns a new list where all the odd numbers are removed.

    Args:
        lst (list): a list of number.
    
    Returns:
        list: list without odd numbers.
    '''
    list1=[]
    for i in range(len(lst)):
        if lst[i]%2==0:
            list1.append(lst[i])
    return list1
print(remove_odd([1,2,3,4,4,6,7,7,8]))
