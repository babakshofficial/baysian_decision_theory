import numpy as np
import math

def d_dim_calculate(x, dim, mean, cov_matrix):
    P = 1 / (((2 * math.pi) ^ dim/2) * (np.linalg.det(cov_matrix)) ^ 0.5) * math.exp((-1 * 0.5) * np.matrix.transpose(x - mean) * (np.linalg.inv(cov_matrix)) * (x - mean))
    return P

def one_dim_calculate(x, mean, variance):
    P = 1 / math.sqrt(2 * math.pi * variance) * math.exp(-1 * (((x - mean) ** 2) / (2 * variance)))
    return P
