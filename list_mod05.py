def square(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list of all numbers are squared.
    '''
    list1=[]
    for i in range(len(lst)):
            x=lst[i]**2
            list1.append(x)
    return list1
print(square([1,2,3,4,4,6,7,7,8]))