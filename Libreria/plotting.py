import numpy as np
import matplotlib.pyplot as plt

def sturges (N_events) :
    return int(np.ceil(1 + 3.322 * np.log (N_events)))