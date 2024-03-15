#!/usr/bin/python

from numpy import exp, log

def exp_pdf (x, tau) :
    '''
    the exponential probability density function
    '''
    if tau == 0. :
      return 1.
    return exp (-1 * x / tau) / tau

def likelihood (theta, pdf, sample) :
    '''
    the likelihood function calculated
    for a sample of independent variables idendically distributed 
    according to their pdf with parameter theta
    '''
    risultato = 1.
    for x in sample:
      risultato = risultato * pdf (x, theta)
    return risultato

def loglikelihood (theta, pdf, sample) :
    '''
    the log-likelihood function calculated
    for a sample of independent variables idendically distributed 
    according to their pdf with parameter theta
    '''
    risultato = 0.
    for x in sample:
      if (pdf (x, theta) > 0.) : risultato = risultato + log (pdf (x, theta))    
    return risultato