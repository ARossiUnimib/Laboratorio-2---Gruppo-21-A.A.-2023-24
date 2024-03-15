#!/usr/bin/python

def write(name, values):
    """
    save a list of values 
    
    values: variables to be saved
    name:   the name of the written wile 
    """
    with open (name, 'w') as fp :
        for item in values:
            fp.write(str (item) + '\n')

def read_floats(name):
    """
    Read numbers from file one for each line
    """
    with open(name) as f:
        sample = [float (x) for x in f.readlines()]

    return sample