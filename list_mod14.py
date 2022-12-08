def replace_minimun_with_0(lst):
    """Given the list of numbers, Replace the mininum numbers in the list with 0.

    Args:
        lst (list): list of numbers
    Returns: 
        list: list minimum numbers are replaced with 0
    """
    mn=lst[0]
    for i in range(len(lst)):
        if mn>lst[i]:
            mn=lst[i]
    lst.pop(lst.index(mn))
    lst.insert(0,0)
    return lst
print(replace_minimun_with_0([1,2,3,4,5,6,7]))