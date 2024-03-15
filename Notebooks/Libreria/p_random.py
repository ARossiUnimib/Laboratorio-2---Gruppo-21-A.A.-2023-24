#!/usr/bin/python

import random
from numpy import sqrt, log

def generate_uniform(N, seed=0.):
    '''
    Generation of N pseudo-random numbers distributed between 0 and 1
    starting from a given seed
    '''
    if seed != 0.:
        random.seed(float(seed))
    randlist = []
    for i in range(N):
        # Return the next random floating point number in the range 0.0 <= X < 1.0
        randlist.append(random.random())
    return randlist

def rand_range(xMin, xMax):
    '''
    Generation of a pseudo-random number distributed between xMin and xMax
    '''
    return xMin + random.random() * (xMax - xMin)

def generate_range(xMin, xMax, N, seed=0.):
    '''
    Generation of N pseudo-random numbers distributed between xMin and xMax
    starting from a given seed
    '''
    if seed != 0.:
        random.seed(float(seed))
    randlist = []
    for i in range(N):
        # Return the next random floating point number in the range xMin <= X < xMax
        randlist.append(rand_range(xMin, xMax))
    return randlist

def rand_TAC(f, xMin, xMax, yMax):
    '''
    Generation of a pseudo-random number using the try and catch method
    '''
    x = rand_range(xMin, xMax)
    y = rand_range(0, yMax)
    while y > f(x):
        x = rand_range(xMin, xMax)
        y = rand_range(0, yMax)
    return x

def generate_TAC(f, xMin, xMax, yMax, N, seed=0.):
    '''
    Generation of N pseudo-random numbers using the try and catch method, within a certain range,
    starting from a given seed
    '''
    if seed != 0.:
        random.seed(float(seed))
    randlist = []
    for i in range(N):
        randlist.append(rand_TAC(f, xMin, xMax, yMax))
    return randlist

def rand_TCL(xMin, xMax, N_sum=10):
    '''
    Generation of a pseudo-random number using the central limit theorem method
    on a fixed interval
    '''
    y = 0.
    for i in range(N_sum):
        y += rand_range(xMin, xMax)
    y /= N_sum
    return y

def generate_TCL(xMin, xMax, N, N_sum=10, seed=0.):
    '''
    Generation of N pseudo-random numbers using the central limit theorem method, within a certain range,
    starting from a given seed
    '''
    if seed != 0.:
        random.seed(float(seed))
    randlist = []
    for i in range(N):
        randlist.append(rand_TCL(xMin, xMax, N_sum))
    return randlist

def rand_TCL_ms(mean, sigma, N_sum=10):
    '''
    Generation of a pseudo-random number using the central limit theorem method
    given the mean and sigma of the Gaussian
    '''
    y = 0.
    delta = sqrt(3 * N_sum) * sigma
    xMin = mean - delta
    xMax = mean + delta
    for i in range(N_sum):
        y += rand_range(xMin, xMax)
    y /= N_sum
    return y

def generate_TCL_ms(mean, sigma, N, N_sum=10, seed=0.):
    '''
    Generation of N pseudo-random numbers using the central limit theorem method, given the mean and sigma of the Gaussian,
    starting from a given seed
    '''
    if seed != 0.:
        random.seed(float(seed))
    randlist = []
    delta = sqrt(3 * N_sum) * sigma
    xMin = mean - delta
    xMax = mean + delta
    for i in range(N):
        randlist.append(rand_TCL(xMin, xMax, N_sum))
    return randlist

def inv_exp(y, lamb=1):
    '''
    Inverse of the primitive of the exponential PDF.
    pdf(x) = lambda * exp(-lambda x) for x >= 0, 0 otherwise.
    F(x) = int_{0}^{x} pdf(x)dx = 1 - exp(-lambda * x) for x >= 0, 0 otherwise.
    F^{-1}(y) = - (ln(1-y)) / lambda
    '''
    return -1 * log(1 - y) / lamb

def rand_exp(tau):
    '''
    Generation of a pseudo-random exponential number
    using the inverse function method
    based on the exponential tau
    '''
    lamb = 1. / tau
    return inv_exp(random.random(), lamb)

def generate_exp(tau, N, seed=0.):
    '''
    Generation of N pseudo-random exponential numbers
    using the inverse function method, given the exponential tau,
    starting from a given seed
    '''
    if seed != 0.:
        random.seed(float(seed))
    randlist = []
    for i in range(N):
        randlist.append(rand_exp(tau))
    return randlist

def rand_poisson(mean):
    '''
    Generation of a pseudo-random Poisson number
    based on an exponential pdf
    '''
    total_time = rand_exp(1.)
    events = 0
    while total_time < mean:
        events += 1
        total_time += rand_exp(1.)
    return events

def generate_poisson(mean, N, seed=0.):
    '''
    Generation of N pseudo-random Poisson numbers
    based on an exponential pdf
    '''
    if seed != 0.:
        random.seed(float(seed))
    randlist = []
    for i in range(N):
        randlist.append(rand_poisson(mean))
    return randlist