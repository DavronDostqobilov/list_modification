def square_and_remove_positive(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the positive numbers are removed.
    
    Args:
        lst (list): list of numbers.
    
    Returns:
        list: list of all non-negative numbers ared squared.
    '''
    list1=[]
    for i in range(len(lst)):
        if lst[i]<0:
            x=lst[i]**2
            list1.append(x)
    return list1
print(square_and_remove_positive([5,2,-3,-4]))