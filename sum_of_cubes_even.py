def sum_of_cubes_even(n):
    ### Replace with your own code (begin) ###
    if not isinstance(n, int) or n<0:
        return -1
    if n>2000:
        print("Warning: n is large, computation may take some time.")
    total = 0.0
    for i in range(0, n+1, 2):
            total +=i**3
    return total
    ### Replace with your own code (end)   ###
