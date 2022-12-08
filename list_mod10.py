def square_and_remove_divisible_by_3(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the numbers that are divisible by 3 are
    
    Args:
        lst (list): list of numbers.
    
    Returns:
        list: list of all numbers are not divisible by 3.
    '''
    list1=[]
    for i in range(len(lst)):
        if lst[i]%3!=0:
            x=lst[i]**2
            list1.append(x)
    return list1
print(square_and_remove_divisible_by_3([1,2,3,4,5,6,6,7,8,9]))