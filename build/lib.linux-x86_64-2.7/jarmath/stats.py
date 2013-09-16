""" Authored by Raj Maitra

    Statistics Module for JarMath Package.





"""
from math import *
from numpy import *

def linear_regression_slope(price):
    """ This function determines the slope of an array of prices.

    Arguments:
        price: array of historical stock prices.
    
    Returns:
        slope: The slope of the price history.
        sigma: the standard deviation of the price history.

    """
    y = log(price)
    x = log(arange(len(y)) + 1)
    xy = x*y
    N = len(y)
    m1 = sum(xy)-(sum(x)*sum(y))/N
    m2 = sum(x*x)-(sum(x)**2)/N
    slope = m1/m2
    sigma = std(y)
    return slope, sigma

