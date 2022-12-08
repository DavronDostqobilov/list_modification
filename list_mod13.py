def replace_maximum_with_0(lst):
    """Given the list of numbers, Replace the maximum numbers in the list with 0.

    Args:
        lst (list): list of numbers
    Returns: 
        list: list maximum numbers are replaced with 0
    """
    mx=0
    for i in range(len(lst)):
        if mx<lst[i]:
            mx=lst[i]
    lst.pop(lst.index(mx))
    lst.append(0)
    return lst
print(replace_maximum_with_0([1,2,3,4,5,6,7]))