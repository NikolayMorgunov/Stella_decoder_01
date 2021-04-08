import numpy as np


def find_synchro_in_line(line):
    synchro_w = 98
    for i in range(len(line) - synchro_w):
        peacks_y = [line[i], line[i]]
        peacks_x = [i, i]
        for j in range(1, synchro_w):
            if abs(line[i + j] - peacks_y[-2]) > abs(peacks_y[-1] - peacks_y[-2]) or abs(
                    line[i + j] - peacks_y[-2]) < 20:
                peacks_y[-1] = line[i + j]
                peacks_x[-1] = i + j
            else:
                peacks_y.append(peacks_y[-1])
                peacks_x.append(peacks_x[-1])

        if 90 < (peacks_x[-1] - peacks_x[0]) < 100 and 15 <= len(peacks_x) < 17:
            return i
    return None


def find_synchro(fs, data):
    frame_width = int(0.5 * fs)
    w, h = frame_width, len(data) // frame_width
    max_d = max(data)
    data = [i * 255 // max_d for i in data]
    matrix = []

    for i in range(h):
        cur = []
        for j in range(w):
            cur.append(data[i * w + j])
        matrix.append(cur)

    for i in range(len(matrix)):
        id = i - 500 + 1206
        matrix[i] = matrix[i][id:] + matrix[i][:id]

    data = []
    for i in range(h):
        for j in range(w):
            data.append(matrix[i][j])


    return data
