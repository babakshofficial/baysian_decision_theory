import numpy as np
import math

def d_dim_calculate(x, dim, mean_vector, cov_matrix):
    P = 1 / (((2 * math.pi) ^ dim/2) * (np.linalg.det(cov_matrix)) ^ 0.5) * math.exp((-1 * 0.5) * np.matrix.transpose(x - mean_vector) * (np.linalg.inv(cov_matrix)) * (x - mean_vector))
    return P

def one_dim_calculate(x, mean_vector, variance):
    P = 1 / math.sqrt(2 * math.pi * variance) * math.exp(-1 * (((x - mean_vector) ** 2) / (2 * variance)))
    return P
