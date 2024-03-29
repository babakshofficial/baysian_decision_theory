import numpy as np
import math

# created by Babak Shahriari
# this class make likelihood values based on gaussian
# distribution for when Covariance matrix isn't singular

def d_dim_calculate(x, dim, mean, cov_matrix):
    coef1 = (2 * math.pi) ** (dim / 2)
    coef2 = np.linalg.det(cov_matrix) ** (1/2)
    coef = coef1 * coef2
    transpose = (np.subtract(x,mean)).T
    inv = np.linalg.inv(cov_matrix)
    sub = np.subtract(x,mean)
    second_part = np.dot(np.dot(transpose,inv),sub)
    P = (1/coef) * np.exp(((-1)/2) * second_part)
    return P

def one_dim_calculate(x, mean, variance):
    P = 1 / math.sqrt(2 * math.pi * variance) * math.exp(-1 * (((x - mean) ** 2) / (2 * variance)))
    return P