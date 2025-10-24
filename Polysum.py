def polysum(n,s):
    '''
    n: number of sides.
    s: length of each side.
    This function should sum the area and square of the perimeter of the regular polygon. 
    The function returns the sum, rounded to 4 decimal places.
    '''
    import math
    a=0.25*n*s**2/(math.tan(math.pi/n))
    p=n*s
    return(round(a+p**2,4))