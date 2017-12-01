# -*- coding: utf-8 -*-


from PIL import Image
from math import pi, log, exp
import numpy as np
import sys

def main(filename, r):
    # должна обрабатывать чб файл <filename> в формате PNG, уравнивать гистограмму
    # и записывать результат в <filename>.equalized.png
    img = Image.open(filename)
    img.load()

    a = np.array(img.getdata(), dtype=np.uint8)
    a = a[:,0]
    a=a.reshape(img.size[::-1])
    b = np.zeros(img.size[::-1], dtype=np.uint8)
    h, w = a.shape
    # код сюда ....

    hi = np.zeros(256)
    for i in range (h):
        for j in range (w):
            h[a[i][j]]= h[a[i][j]]+1
    hist = np.array(hi)/(h*w)

    cdf = np.cumsum(hist)

    sk = np.uint8(255 * cdf)

    h,w = a.shape

    for i in range(0,h):
        for j in range(0,w):
            b[i, j]=sk[a[i,j]]

    newimg = Image.fromarray(b);
    newimg.show()
    newimg.save(filename + '.equalized.png')

if __name__ == '__main__':
    # Запускать с командной строки с аргументом <имя файла>, например: python gauss.py darwin.png
    if len(sys.argv) > 1:
        main(sys.argv[1], r=3)
    else:
        print("Must give filename.\n")



