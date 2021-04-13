def to_matrix(fs, data):
    frame_width = int(0.5 * fs)
    w, h = frame_width, len(data) // frame_width
    matrix = []

    for i in range(h):
        cur = []
        for j in range(w):
            cur.append(data[i * w + j])
        matrix.append(cur)
    return matrix
