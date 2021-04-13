from PIL import Image
import matplotlib.pyplot as plt


def draw(fs, data_am):
    frame_width = int(0.5 * fs)
    w, h = frame_width, len(data_am) // frame_width
    image = Image.new('RGB', (w, h))

    px, py = 0, 0
    for p in range(len(data_am)):
        lum = int(data_am[p])
        if lum < 0: lum = 0
        if lum > 255: lum = 255
        image.putpixel((px, py), (lum, lum, lum))
        px += 1
        if px >= w:
            if (py % 50) == 0:
                print(f"Line saved {py} of {h}")
            px = 0
            py += 1
            if py >= h:
                break
    image = image.resize((w, 3 * h))
    # for i in range(w):
    #      print(data_am[200 * w + i])
    # print()
    # print()
    # print()
    # print()
    # for i in range(w):
    #      print(data_am[1000 * w + i])
    image.save('Izobrazhenie so spootnika.png')
