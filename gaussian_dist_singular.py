import numpy as np
import math

def singular(data, mean, cov_matrix):
    eig_values = np.linalg.eig(np.multiply((2 * math.pi), cov_matrix))
    np.linalg.det(np.multiply(eig_values[0],eig_values[1]))
    pseudo_determinent = np.linalg.det(np.linalg.pinv(cov_matrix))
    transpose = (np.subtract(data, mean)).T
    pinv = np.linalg.pinv(cov_matrix)
    sub = np.subtract(data, mean)
    second_part = np.dot(np.dot(transpose, pinv), sub)
    P = pseudo_determinent * np.exp(((-1) / 2) * second_part)
    return P