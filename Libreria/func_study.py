#!/usr/bin/python

def bisection(g, xMin, xMax, prec=0.0001):
    """
    Function that calculates roots
    using the bisection method.

    Parameters:
    - g (function): The function to find the root of.
    - xMin (float): Minimum of the interval.
    - xMax (float): Maximum of the interval.
    - prec (float): Precision of the function.

    Returns:
    float: The root of the function within the specified interval.
    """

    xAve = xMin 
    while (xMax - xMin) > prec:
        xAve = 0.5 * (xMax + xMin) 
        if g(xAve) * g(xMin) > 0.:
            xMin = xAve 
        else:
            xMax = xAve 
    return xAve 

def recursive_bisection(g, xMin, xMax, prec=0.0001):
    """
    Function that calculates roots
    using the recursive bisection method.

    Parameters:
    - g (function): The function to find the root of.
    - xMin (float): Minimum of the interval.
    - xMax (float): Maximum of the interval.
    - prec (float): Precision of the function.

    Returns:
    float: The root of the function within the specified interval.
    """

    xAve = 0.5 * (xMax + xMin)
    if (xMax - xMin) < prec:
        return xAve
    if g(xAve) * g(xMin) > 0.:
        return recursive_bisection(g, xAve, xMax, prec)
    else:
        return recursive_bisection(g, xMin, xAve, prec)

def goldenSectionMin(g, x0, x1, prec=0.0001):
    """
    Function that calculates the minimum value
    using the golden section method.

    Parameters:
    - g (function): The function to find the minimum value of.
    - x0 (float): Lower end of the interval.
    - x1 (float): Upper end of the interval.
    - prec (float): Precision of the function.

    Returns:
    float: The minimum value of the function within the specified interval.
    """

    r = 0.618
    x2 = 0.
    x3 = 0. 
    width = abs(x1 - x0)
     
    while width > prec:
        x2 = x0 + r * (x1 - x0) 
        x3 = x0 + (1. - r) * (x1 - x0)  
      
        if g(x3) > g(x2): 
            x0 = x3
            x1 = x1         
        else:
            x1 = x2
            x0 = x0          
            
        width = abs(x1 - x0)             
                                   
    return (x0 + x1) / 2. 

def recursive_goldenSectionMin(g, x0, x1, prec=0.0001):
    """
    Function that calculates the minimum value
    using the recursive golden section method.

    Parameters:
    - g (function): The function to find the minimum value of.
    - x0 (float): Lower end of the interval.
    - x1 (float): Upper end of the interval.
    - prec (float): Precision of the function.

    Returns:
    float: The minimum value of the function within the specified interval.
    """

    r = 0.618
    x2 = x0 + r * (x1 - x0)
    x3 = x0 + (1. - r) * (x1 - x0) 
    width = abs(x1 - x0)

    if width < prec:
        return (x0 + x1) / 2.
    elif g(x3) > g(x2):
        return recursive_goldenSectionMin(g, x3, x1, prec)
    else:
        return recursive_goldenSectionMin(g, x0, x2, prec)   

def goldenSectionMax(g, x0, x1, prec=0.0001):
    """
    Function that calculates the maximum value
    using the golden section method.

    Parameters:
    - g (function): The function to find the maximum value of.
    - x0 (float): Lower end of the interval.
    - x1 (float): Upper end of the interval.
    - prec (float): Precision of the function.

    Returns:
    float: The maximum value of the function within the specified interval.
    """

    r = 0.618
    x2 = 0.
    x3 = 0. 
    width = abs(x1 - x0)
     
    while width > prec:
        x2 = x0 + r * (x1 - x0) 
        x3 = x0 + (1. - r) * (x1 - x0)  
      
        if g(x3) < g(x2): 
            x0 = x3
            x1 = x1         
        else:
            x1 = x2
            x0 = x0          
            
        width = abs(x1 - x0)             
                                   
    return (x0 + x1) / 2. 

def recursive_goldenSectionMax(g, x0, x1, prec=0.0001):
    """
    Function that calculates the maximum value
    using the recursive golden section method.

    Parameters:
    - g (function): The function to find the maximum value of.
    - x0 (float): Lower end of the interval.
    - x1 (float): Upper end of the interval.
    - prec (float): Precision of the function.

    Returns:
    float: The maximum value of the function within the specified interval.
    """

    r = 0.618
    x2 = x0 + r * (x1 - x0)
    x3 = x0 + (1. - r) * (x1 - x0) 
    width = abs(x1 - x0)

    if width < prec:
        return (x0 + x1) / 2.
    elif g(x3) < g(x2):
        return recursive_goldenSectionMax(g, x3, x1, prec)
    else:
        return recursive_goldenSectionMax(g, x0, x2, prec)
