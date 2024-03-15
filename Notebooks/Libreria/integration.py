#!/usr/bin/python

from p_random import generate_range, rand_range
from numpy import sqrt

def integral_HOM(func, xMin, xMax, yMax, N_evt):
    x_coord = generate_range(xMin, xMax, N_evt)
    y_coord = generate_range(0., yMax, N_evt)

    points_under = 0
    for x, y in zip(x_coord, y_coord):
        if func(x) > y:
            points_under += 1 

    A_rect = (xMax - xMin) * yMax
    frac = float(points_under) / float(N_evt)
    integral = A_rect * frac
    integral_unc = A_rect**2 * frac * (1 - frac) / N_evt
    return integral, integral_unc

def integral_CrudeMC(g, xMin, xMax, N_rand):
    sum = 0.
    sum_sq = 0.    
    for i in range(N_rand):
       x = rand_range(xMin, xMax)
       sum += g(x)
       summ_sq += g(x) * g(x)     
     
    mean = sum / float(N_rand)
    variance = sum_sq / float(N_rand) - mean * mean 
    variance = variance * (N_rand - 1) / N_rand
    length = (xMax - xMin)
    return mean * length, sqrt(variance / float(N_rand)) * length
