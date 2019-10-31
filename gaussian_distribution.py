import numpy as np
import math

def calculate(x, dim, mean_vector, cov_matrix):
    P = 1 / (((2 * math.pi) ^ dim/2) * (np.linalg.det(cov_matrix)) ^ 0.5) * math.exp()
    return 1