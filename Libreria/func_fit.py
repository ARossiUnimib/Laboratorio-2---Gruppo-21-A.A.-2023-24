#!/usr/bin/python

import numpy as np
from scipy.integrate import quad
from iminuit import Minuit
from iminuit.cost import LeastSquares, ExtendedBinnedNLL, UnbinnedNLL
import matplotlib.pyplot as plt
from plotting import sturges

def plot_model(x_values, cdf):
    """
    Plots the probability mass function (PMF) of a discrete distribution given the cumulative distribution function (CDF).

    Parameters:
    - x_values (array-like): Values of the random variable.
    - cdf (array-like): Cumulative distribution function values corresponding to the x_values.

    Note:
    The function assumes that the input represents a discrete distribution, and it uses the differences
    between consecutive CDF values to plot the PMF with a stepwise appearance.
    """
    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot(x_values, np.append(np.diff(cdf), np.nan), drawstyle="steps-post")


def fancy_print(minuit: Minuit):
    if minuit.valid:
        print("Fitting was successfull")
    
        for par, val, err in zip (minuit.parameters, minuit.values, minuit.errors):
            print(f"{par} = {val:.3f} +- {err:.3fz}")

    else:
        print("Fitting failed")

def compute_cdf(pdf, x_values, *params):
    """
    Compute the cumulative distribution function (CDF) of a given probability density function (PDF)
    with parameters.

    Parameters:
    - pdf: Probability density function (function)
    - x_values: values for which to compute the CDF
    - params: Parameters of the PDF

    Returns:
    - cdf_values: Cumulative distribution function values for the input x_values
    """
    cdf_values = [quad(pdf, -np.inf, x, args=params)[0] for x in x_values]
    return np.array(cdf_values)

def binned_fit(sample, cdf, initial_params, names, N_bins= -1):
    """
    Perform a binned fit using the iminuit package.

    Parameters:
    - sample (array-like): Input data sample for the fit.
    - cdf (callable): Cumulative Distribution Function (CDF) to fit against.
    - initial_params (tuple or array-like): Initial values for the fit parameters.
    - names (list of str): Names of the fit parameters.
    - N_bins (int, optional): Number of bins for the histogram. If -1, determined by Sturges' rule.

    Returns:
    - Minuit: Minuit object initialized for the binned fit.

    Important note:
    The binned_fit function uses ExtendedBinnedNLL: not-normalized histogram fit
    """

    N_events = len(sample)

    if (N_bins == -1):
        N_bins = sturges(N_events)

    bin_content, bin_edges = np.histogram(sample, bins=N_bins)

    my_cost_func = ExtendedBinnedNLL(bin_content, bin_edges, cdf)

    return Minuit(my_cost_func, *initial_params, name=names)

def unbinned_fit(sample, expected_pdf, initial_params, names):
    """
    Perform an unbinned fit using the iminuit package.

    Parameters:
    - sample (array-like): Input data sample for the fit.
    - expected_pdf (callable): Probability density function (PDF) to fit against.
    - initial_params (tuple or array-like): Initial values for the fit parameters.
    - names (list of str): Names of the fit parameters.

    Important notes:
    Binned fitting method is preferred to the unbinned one
    """

    my_cost_func_unb = UnbinnedNLL(sample, expected_pdf)

    return Minuit(my_cost_func_unb, *initial_params, name=names)

def ls_binned_fit(sample, pdf, initial_params, names, N_bins=-1):
    """
    Perform a least-squares binned fit using the iminuit package.

    Parameters:
    - sample (array-like): Input data sample for the fit.
    - pdf (callable): Probability density function (PDF) to fit against.
    - initial_params (tuple or array-like): Initial values for the fit parameters.
    - names (list of str): Names of the fit parameters.
    - N_bins (int, optional): Number of bins for the histogram. If -1, determined by Sturges' rule.

    Returns:
    - Minuit: Minuit object initialized for the least-squares binned fit.
    """
    N_events = len(sample)

    if N_bins == -1:
        N_bins = sturges(N_events)

    min_value = min(sample)
    max_value = max(sample)
    bin_width = (max_value - min_value) / N_bins

    bin_content, _ = np.histogram(sample, bins=N_bins)

    # Define an approximation function representing the expected values with the 
    # specified parameters in a bin
    def func_approx(x, N_events, bin_width, *params):
        return N_events * pdf(x, *params) * bin_width

    # Calculate bin centers
    bin_centers = min_value + np.arange(N_bins) * bin_width

    # Using Neyman's approximation (sigma**2 = N)
    sigma_y = [max(np.sqrt(num), 1.) for num in bin_content]

    least_squares = LeastSquares(bin_centers, bin_content, sigma_y, func_approx)

    return Minuit(least_squares, *initial_params, name=names)
