def count_digits_greater_than(n, t):
    ### Replace with your own code (begin) ###
    if not isinstance(n, int) or not isinstance(t, int):
        return -1
    if n<0 or t<0 or t>9:
        return -1
    count = 0
    for digit in str(n):
        if int(digit)>t:
            count+= 1
    return count
    ### Replace with your own code (end)   ###
