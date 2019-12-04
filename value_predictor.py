def value_predictor(num):
    """Return the middle value of list that have increasing element
    Parameters
    ----------
    num : list
          List of increasing number

    Returns
    -------
    Output  : float
              the middle value of a list number
    """
    return 0.5*(num[int(len(num)/2)-1]+num[int(len(num)/2)])


print(value_predictor([1, 2, 3, 4, 5, 6]))
