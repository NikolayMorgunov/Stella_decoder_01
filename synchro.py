import numpy as np
from make_matrix import *


def find_synchro(fs, data):
    matrix = to_matrix(fs, data)
    matrix_ans = []
    fst_id = 3000
    k = 0
    for i in matrix:
        for j in range(fst_id, len(i) - 100):
            if j < (len(i) - 7) and i[j] < 70 and i[j + 1] < 70 and \
                    i[j + 2] < 70 and \
                    i[j + 3] < 70 and \
                    i[j + 4] > 70 and i[j + 5] > 70 and i[j + 6] > 70 and i[j + 98] < 70 and i[j + 99] < 70 and i[
                j + 100] < 70:
                matrix[k] = matrix[k][j:] + matrix[k][:j]
                matrix_ans = matrix_ans + i[j:] + i[:j]
                break
    return matrix_ans, matrix
