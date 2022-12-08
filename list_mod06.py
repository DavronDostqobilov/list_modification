def square_and_remove_even(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the even numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list of all even numbers are squared.
    '''
    list1=[]
    for i in range(len(lst)):
        if lst[i]%2==1:
            x=lst[i]**2
            list1.append(x)
    return list1
print(square_and_remove_even([1,2,3,4,5,6,7,8,9]))
    