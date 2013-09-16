""" Written by Raj Maitra

    Filters Module for JarMath Package.



"""
from math import *
from numpy import *

def moving_average(price,N):
    """ This function uses a moving average function to smoothen the price history.

    Arguments:
        price: This is the raw historical prices to be smoothened.
        N: This is the size of the moving average filter.
    
    Returns:
        price_ave: This is the smoothened price signal.

    """
    window = ones(int(N))/float(N)
    price_ave = convolve(price,window,'same')
    return price_ave

def kalman_filter_1d(price, R_var, q_var):
    """ Kalman Smoother 1-Dimensional
    
        The kalman filter uses the black and scholes stochastic differential equation as the model for estimation.
        The 
    
    """	
    P_var = 1
    estimate = price[0]
    price_hat = []
    mu = log(1.05)/365

    for measurement in price:
        residual = measurement - estimate
        K_gain = float(P_var/(P_var+R_var))
        
        estimate = estimate + K_gain*residual
        P_var = (1 - K_gain)*P_var
        P_var = P_var+q_var
        
        estimate = estimate + mu*measurement
        price_hat.append(estimate)

    return price_hat

