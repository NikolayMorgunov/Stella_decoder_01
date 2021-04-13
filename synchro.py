import numpy as np


def find_synchro(fs, data):
    frame_width = int(0.5 * fs)
    w, h = frame_width, len(data) // frame_width
    matrix = []

    for i in range(h):
        cur = []
        for j in range(w):
            cur.append(data[i * w + j])
        matrix.append(cur)

    matrix_ans = []
    fst_id = 3000
    for i in matrix:
        for j in range(fst_id, len(i) - 100):
            if j < (len(i) - 7) and i[j] < 70 and i[j + 1] < 70 and \
                    i[j + 2] < 70 and \
                    i[j + 3] < 70 and \
                    i[j + 4] > 70 and i[j + 5] > 70 and i[j + 6] > 70 and i[j + 98] < 70 and i[j + 99] < 70 and i[j + 100] < 70:
                matrix_ans = matrix_ans + i[j:] + i[:j]
                break
    return matrix_ans
