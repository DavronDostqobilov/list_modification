def remove_even(lst):
    '''Given a list of numbers, write a function that returns a new list where all the even numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without even numbers.
    '''
    list1=[]
    for i in range(len(lst)):
        if lst[i]%2==1:
            list1.append(lst[i])
    return list1
print(remove_even([1,2,3,4,4,6,7,7,8]))