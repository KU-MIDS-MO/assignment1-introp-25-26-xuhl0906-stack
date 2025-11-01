def is_strictly_increasing_digits(n):
    ### Replace with your own code (begin) ###
    if not isinstance(n, int) or n<0:
        return -1
    s=str(n)
    if len(s)<=1:
        return True
    for i in range(1, len(s)):
        if int(s[i])<=int(s[i-1]):
            return False
    return True
    ### Replace with your own code (end)   ###